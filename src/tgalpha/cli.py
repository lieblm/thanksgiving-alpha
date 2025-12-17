import typer
from pathlib import Path
from typing import List, Tuple
import yaml
import pandas as pd

from .config import Config
from .universe import load_universe
from .data_providers.yahoo import YahooProvider
from .stats import holiday_window_dates, compute_return
from .ranking import aggregate_per_symbol
from .report import export_tables
from .coverage import compute_coverage_by_year, format_coverage_table

app = typer.Typer()


@app.command()
def main(
    config: str,
    top: int = 20,
    statistics: bool = True,
    show_coverage: bool = False,
) -> None:
    """Run the Thanksgiving seasonality analysis with statistical significance tests.

    Args:
        config: Path to YAML configuration file
        top: Number of top-ranked symbols to display
        statistics: Compute bootstrap CIs and significance tests (default: True)
        show_coverage: Display year-by-year data coverage table
    """
    # Load configuration
    cfg = Config(**yaml.safe_load(Path(config).read_text()))

    # Load universe of symbols
    symbols = load_universe(cfg.universe)

    # Initialize data provider
    prov = YahooProvider()

    # Collect returns for each symbol and year
    rows: List[Tuple[str, int, float]] = []

    print(f"Analyzing {len(symbols)} symbols from {cfg.start_year} to {cfg.end_year}...")

    for year in range(cfg.start_year, cfg.end_year + 1):
        try:
            # Calculate window dates for this year
            open_day, close_day = holiday_window_dates(
                year, cfg.window.days_before, cfg.window.days_after, cfg.holiday
            )

            # Add buffer for data download (±7 calendar days)
            start = (open_day - pd.Timedelta(days=7)).date()
            end = (close_day + pd.Timedelta(days=7)).date()

            for s in symbols:
                try:
                    # Download OHLC data
                    df = prov.get_ohlc(s, start, end)

                    # Compute return for this window
                    r = compute_return(df, open_day, close_day)

                    if r is not None:
                        rows.append((s, year, r))
                except Exception:
                    # Skip individual symbol errors but continue processing
                    pass  # Silently skip to reduce noise

        except Exception as e:
            print(f"Warning: Failed to process year {year}: {e}")
            continue

    if not rows:
        print("Error: No data collected. Please check your configuration and data availability.")
        raise typer.Exit(code=1)

    unique_symbols = len(set(r[0] for r in rows))
    print(f"Collected {len(rows)} return observations across {unique_symbols} symbols")
    print(
        f"Universe contained {len(symbols)} symbols; {len(symbols) - unique_symbols} excluded (insufficient data)"
    )

    # Show coverage by year if requested
    if show_coverage:
        coverage = compute_coverage_by_year(rows, cfg.start_year, cfg.end_year)
        print("\n" + "=" * 50)
        print("DATA COVERAGE BY YEAR")
        print("=" * 50)
        print(format_coverage_table(coverage))
        print("")

    # Aggregate and rank with statistical tests
    ranking = aggregate_per_symbol(
        rows,
        min_trades=cfg.ranking.min_trades,
        compute_statistics=statistics,
        confidence_level=0.95,
    )

    # Export results
    out_dir = Path(cfg.output.dir)
    export_tables(ranking, out_dir, cfg.output.formats)

    # Display top N with significance indicators
    print(f"\nTop {top} symbols by median return:")
    display_df = ranking.head(top).to_pandas()

    # Format display columns
    if statistics and "significant" in display_df.columns:
        # Add significance indicator
        display_df["sig"] = display_df["significant"].apply(lambda x: "***" if x else "")

        # Select key columns for display
        display_cols = [
            "symbol",
            "n",
            "median_return",
            "win_rate",
            "p_value_corrected",
            "sig",
            "sharpe",
        ]
        display_cols = [c for c in display_cols if c in display_df.columns]

        print(display_df[display_cols].to_string(index=False))
        print("\n*** = Statistically significant after Benjamini-Hochberg correction (FDR < 0.05)")
    else:
        print(display_df.to_string(index=False))

    print(f"\nFull results saved to {out_dir}/")

    if statistics:
        sig_count = ranking["significant"].sum() if "significant" in ranking.columns else 0
        total_count = len(ranking)
        print("\nStatistical Summary:")
        print(
            f"  - {sig_count} of {total_count} stocks show statistically significant positive returns"
        )
        print(
            f"  - {sig_count/total_count*100:.1f}% pass significance test (Wilcoxon + BH correction)"
        )


if __name__ == "__main__":
    app()
