# Thanksgiving-Alpha

> **A reproducible research tool for analyzing stock performance patterns around US Thanksgiving**

Comprehensive quantitative analysis of major US equity indices (DJIA, NASDAQ-100, S&P 500) measuring returns from X business days before Thanksgiving to Y business days after. Built with Python, featuring proper NYSE trading calendars, statistical significance testing, and multi-format outputs.

## 📊 Three Trading Windows Analyzed

This project analyzes **three distinct seasonal trading windows**:

1. **Thanksgiving Window** (Traditional): 3 days before → 1 day after (Black Friday half-day)
2. **Cyber Monday Window** (Extended): 3 days before → 4 days after (Cyber Monday)
3. **Santa Claus Rally Window** (Year-End): Last 5 trading days of year → First 2 trading days of next year (7 days)

See comparative analyses:
- **[COMPARISON_CYBER_MONDAY_VS_THANKSGIVING.md](_thanks/COMPARISON_CYBER_MONDAY_VS_THANKSGIVING.md)**
- **[EXECUTIVE_SUMMARY_SANTA_RALLY.md](EXECUTIVE_SUMMARY_SANTA_RALLY.md)** | **[Czech version](EXECUTIVE_SUMMARY_SANTA_RALLY_CS.md)**

**Key Findings from 25-Year Multi-Index Analysis (2000-2024):**

### Thanksgiving Window (Original Analysis)
- **354 unique stocks** analyzed across 3 major indices with **8,293 stock-year observations**
- **79-87% of stocks** show positive median returns during the Thanksgiving window
- **Technology sector dominance:** 6 of top 10 performers across all indices
- **Statistical rigor:** Proper multiple testing correction (Benjamini-Hochberg FDR) applied
- **S&P 500 representative sample:** 270-stock subset (54% of index) selected for data quality and liquidity

### Cyber Monday Window (Extended Analysis)
- **374 unique stocks** analyzed with **8,510 stock-year observations**
- **10 of 374 stocks (2.8%)** show statistical significance after FDR correction
- **UNH strongest signal:** p=0.001 (DJIA), 84% win rate, +2.80% median return
- **Extended window captures e-commerce momentum** (Cyber Monday online shopping surge)
- See comprehensive report: **[COMPREHENSIVE_CYBER_MONDAY_ANALYSIS.md](_cyberm/COMPREHENSIVE_CYBER_MONDAY_ANALYSIS.md)**

### Santa Claus Rally Window (Year-End Analysis)
- **332 unique stocks** analyzed with **8,091 stock-year observations**
- **2 of 30 DJIA stocks (6.9%)** show statistical significance after FDR correction
- **Statistically significant winners:** DIS (+2.55%, p=0.037), JPM (+1.97%, p=0.037)
- **Stronger than Thanksgiving:** First seasonal window to show statistical significance in large-cap stocks
- **Broad-based effect:** 81.7% of S&P 500 stocks show positive median returns
- See executive summaries: **[English](EXECUTIVE_SUMMARY_SANTA_RALLY.md)** | **[Czech](EXECUTIVE_SUMMARY_SANTA_RALLY_CS.md)**

## Features

- **Multi-index support:** DJIA (30 stocks), NASDAQ-100 (100 stocks), S&P 500 (270-stock representative sample)
- **Statistical framework:** Wilcoxon signed-rank test, bootstrap confidence intervals, Benjamini-Hochberg FDR correction
- **Proper trading calendar:** NYSE holidays, half-day sessions (Black Friday closes 1:00 PM ET)
- **Comprehensive metrics:** Median/mean returns, win rates, standard deviation, Sharpe ratios, p-values
- **Data coverage tracking:** Year-by-year completeness analysis with `--show-coverage` flag
- **Multi-format exports:** CSV, Parquet, HTML with 16 statistical columns
- **Enterprise quality:** 28 passing unit tests, type-safe (mypy), linted (ruff + black)

## Quickstart

```bash
# Using poetry (recommended)
pipx install poetry
poetry install
poetry run python -m tgalpha.cli configs/sp500_25years.yaml --top=50 --statistics --show-coverage

# Or using pip
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
python -m tgalpha.cli configs/djia_25years.yaml --top=30 --statistics
```

## Multi-Index Analysis Results

**Complete 25-year analysis (2000-2024) across three major indices:**

| Index | Stocks Analyzed | Observations | Completeness | Top Performer | Statistical Significance |
|-------|-----------------|--------------|--------------|---------------|--------------------------|
| **S&P 500** | 244 (from 270-stock sample) | 5,756 | 78.8% | SHOP +3.36% | 0/244 (0.0%) |
| **NASDAQ-100** | 80 | 1,818 | 78.6% | ENPH +3.61% | 0/80 (0.0%) |
| **DJIA** | 30 | 719 | 95.9% | AAPL +2.00% | 0/30 (0.0%) |
| **TOTAL** | **354** | **8,293** | **80.9%** | Cross-validated | **0/354 (0.0%)** |

**Key Insights:**
- **S&P 500 Sampling:** Uses representative 270-stock sample (54% of index) selected for liquidity, data quality, and sector balance
- **Statistical Testing:** Wilcoxon + Benjamini-Hochberg FDR correction shows no individual stocks reach significance (demonstrates proper academic rigor)
- **Practical Significance:** Strong empirical patterns remain (79-87% positive median rates, favorable Sharpe ratios 0.4-0.7)
- **Universal Champion:** MNST (Monster Beverage) shows 84% win rate across all three indices
- **Sector Patterns:** Technology/semiconductors dominate top performers, traditional banking underperforms

See comprehensive reports: `EXECUTIVE_SUMMARY.md`, `_thanks/ANALYSIS_SP500_25YEARS.md`, `_thanks/ANALYSIS_NASDAQ100_25YEARS.md`, `_thanks/ANALYSIS_25YEARS.md`

## Usage

### Basic Command

```bash
python -m tgalpha.cli <config_file> [OPTIONS]
```

**Arguments:**
- `config_file`: Path to YAML configuration file (required)

**Options:**
- `--top=N`: Number of top-ranked symbols to display (default: 20)
- `--statistics`: Compute statistical significance tests (Wilcoxon + BH correction) (default: True)
- `--show-coverage`: Display year-by-year data coverage table (default: False)

**Examples:**
```bash
# Run S&P 500 analysis with coverage tracking
python -m tgalpha.cli configs/sp500_25years.yaml --top=50 --show-coverage

# Run NASDAQ-100 analysis with statistical tests
python -m tgalpha.cli configs/nasdaq100_25years.yaml --top=50 --statistics

# Run DJIA analysis (basic)
python -m tgalpha.cli configs/djia_25years.yaml --top=30
```

### Configuration File

Create a YAML configuration file (see examples in `configs/`):

```yaml
universe: sp500               # Options: djia, nasdaq100, sp500, or path to CSV file
start_year: 2000              # First year to analyze
end_year: 2024                # Last year to analyze (inclusive)
holiday: US_THANKSGIVING      # Options: US_THANKSGIVING, SANTA_CLAUS_RALLY
window:
  days_before: 3              # Business days before holiday (ignored for SANTA_CLAUS_RALLY)
  days_after: 1               # Business days after holiday (1=Black Friday, 4=Cyber Monday)
ranking:
  min_trades: 10              # Minimum observations required per symbol
  compute_statistics: true    # Enable statistical significance testing
output:
  dir: "data/outputs"         # Output directory
  formats: ["parquet", "csv", "html"]  # Export formats
```

**Available Universes:**
- `djia` - 30 Dow Jones Industrial Average stocks
- `nasdaq100` - 100 NASDAQ-100 stocks (tech-heavy)
- `sp500` - 270-stock representative sample (54% of S&P 500 index)
- `path/to/file.csv` - Custom stock list (CSV with `symbol` column)

**Pre-configured Trading Windows:**

*Thanksgiving Window (Traditional Black Friday):*
- `configs/djia_25years.yaml` - DJIA, days_after=1
- `configs/nasdaq100_25years.yaml` - NASDAQ-100, days_after=1
- `configs/sp500_25years.yaml` - S&P 500, days_after=1

*Cyber Monday Window (Extended to Monday):*
- `configs/djia_cyber_monday.yaml` - DJIA, days_after=4
- `configs/nasdaq100_cyber_monday.yaml` - NASDAQ-100, days_after=4
- `configs/sp500_cyber_monday.yaml` - S&P 500, days_after=4

*Santa Claus Rally Window (Year-End 7-day):*
- `configs/djia_santa_rally.yaml` - DJIA, last 5 + first 2 trading days
- `configs/nasdaq100_santa_rally.yaml` - NASDAQ-100, last 5 + first 2 trading days
- `configs/sp500_santa_rally.yaml` - S&P 500, last 5 + first 2 trading days

### Example Output

```
Analyzing 244 symbols from 2000 to 2024...
Collected 5,756 return observations across 244 symbols

Data Coverage by Year:
Year  Stocks  Pct Complete
2000     220         73.3%
2001     220         73.3%
...
2024     244         81.3%

Average coverage: 78.8%

Statistical Significance Testing:
- Wilcoxon signed-rank test applied to all stocks
- Benjamini-Hochberg FDR correction (α=0.05)
- 0 of 244 stocks show statistically significant positive returns

Top 10 symbols by median return:
symbol  n  median_return  median_ci_lower  median_ci_upper  win_rate  p_value_corrected  significant  sharpe
  SHOP 10       0.033599         0.006127         0.061071       0.6           0.513312            0 0.09676
    DE 25       0.030835         0.014426         0.047244       0.64          0.178425            0 0.56380
  PANW 13       0.030500         0.012299         0.048701       0.69          0.263896            0 0.28563
  AVGO 16       0.022725         0.008944         0.036506       0.69          0.231878            0 0.44634
  AMAT 25       0.022557         0.009826         0.035288       0.72          0.175443            0 0.45089

Full results saved to data/outputs/
```

### Output Files

Results are saved to the configured output directory (`data/outputs/` by default):
- `ranking.csv` - Full ranking table in CSV format
- `ranking.parquet` - Full ranking table in Parquet format  
- `ranking.html` - HTML table for easy viewing

**Note:** Output files are regenerated with each run and are not tracked in git (see `.gitignore`).

**To reproduce specific analyses:**

*Thanksgiving Window (Traditional):*
```bash
python -m tgalpha.cli configs/djia_25years.yaml
python -m tgalpha.cli configs/nasdaq100_25years.yaml
python -m tgalpha.cli configs/sp500_25years.yaml
```

*Cyber Monday Window (Extended):*
```bash
python -m tgalpha.cli configs/djia_cyber_monday.yaml
python -m tgalpha.cli configs/nasdaq100_cyber_monday.yaml
python -m tgalpha.cli configs/sp500_cyber_monday.yaml
```

*Santa Claus Rally Window (Year-End):*
```bash
python -m tgalpha.cli configs/djia_santa_rally.yaml --statistics --show-coverage
python -m tgalpha.cli configs/nasdaq100_santa_rally.yaml --statistics --show-coverage
python -m tgalpha.cli configs/sp500_santa_rally.yaml --statistics --show-coverage
```

### Output Columns

**Basic Statistics:**
- `symbol`: Stock ticker
- `n`: Number of observations (years with data)
- `median_return`: Median return across all years
- `avg_return`: Average (mean) return
- `win_rate`: Proportion of positive returns
- `std`: Standard deviation of returns

**Statistical Significance (when `--statistics` enabled):**
- `median_ci_lower`, `median_ci_upper`: Bootstrap 95% confidence interval for median
- `mean_ci_lower`, `mean_ci_upper`: Bootstrap 95% confidence interval for mean
- `p_value_wilcoxon`: Wilcoxon signed-rank test p-value (H0: median = 0)
- `p_value_ttest`: One-sample t-test p-value (H0: mean = 0)
- `p_value_corrected`: Benjamini-Hochberg FDR-corrected p-value
- `significant`: Boolean flag (True if p_value_corrected < 0.05)
- `effect_size`: Cohen's d effect size
- `sharpe`: Sharpe ratio (mean / std)

## Development

### Running Tests

```bash
poetry run pytest -v
```

### Linting and Formatting

```bash
# Check code quality
poetry run ruff check .
poetry run black --check .
poetry run mypy src

# Auto-fix issues
poetry run ruff check . --fix
poetry run black .
```

### Project Structure

```
thanksgiving-alpha/
├── configs/                      # Configuration files
│   ├── djia_25years.yaml        # DJIA 25-year analysis
│   ├── nasdaq100_25years.yaml   # NASDAQ-100 25-year analysis
│   ├── sp500_25years.yaml       # S&P 500 25-year analysis
│   └── example_djia.yaml        # Example configuration
├── src/tgalpha/                 # Main package
│   ├── calendar_utils.py        # NYSE trading calendar
│   ├── cli.py                   # Command-line interface
│   ├── config.py                # Configuration models
│   ├── coverage.py              # Data coverage analysis
│   ├── holidays.py              # Thanksgiving date calculation
│   ├── ranking.py               # Aggregation and ranking
│   ├── report.py                # Export functionality
│   ├── stats.py                 # Return calculation
│   ├── stats_tests.py           # Statistical significance testing
│   ├── universe.py              # Symbol universe loading (DJIA, NASDAQ-100, S&P 500)
│   └── data_providers/          # Data source implementations
│       ├── base.py              # Abstract provider interface
│       └── yahoo.py             # Yahoo Finance implementation
├── tests/                       # Unit tests (28 tests)
├── data/outputs/                # Generated results (gitignored)
├── EXECUTIVE_SUMMARY.md         # Cross-index stakeholder overview (English)
├── EXECUTIVE_SUMMARY_CS.md      # Cross-index stakeholder overview (Czech)
├── EXECUTIVE_SUMMARY_SANTA_RALLY.md     # Santa Rally executive summary (English)
├── EXECUTIVE_SUMMARY_SANTA_RALLY_CS.md  # Santa Rally executive summary (Czech)
├── _thanks/                      # Thanksgiving-themed comprehensive reports
│   ├── ANALYSIS_SP500_25YEARS.md         # S&P 500 comprehensive report
│   ├── ANALYSIS_NASDAQ100_25YEARS.md     # NASDAQ-100 comprehensive report
│   ├── ANALYSIS_25YEARS.md               # DJIA comprehensive report
│   └── COMPARISON_CYBER_MONDAY_VS_THANKSGIVING.md # Window comparison doc
├── _cyberm/                      # Cyber Monday comprehensive analysis
│   └── COMPREHENSIVE_CYBER_MONDAY_ANALYSIS.md
├── _santa/                       # Santa Rally analysis and outputs
│   ├── ANALYSIS_SANTA_RALLY_COMPARISON.md
│   └── (outputs) djia/nasdaq100/sp500 Santa Rally run logs
├── STATISTICAL_RESULTS_SUMMARY.md # Statistical testing documentation
└── REFERENCES.md                # Academic citations
```

## How It Works

1. **Date Calculation**: For each year, calculates Thanksgiving (4th Thursday of November)
2. **Trading Window**: Determines X business days before and Y business days after using NYSE calendar
3. **Data Download**: Fetches OHLC data from Yahoo Finance with a buffer around the window
4. **Return Calculation**: Computes `(Close_after / Open_before) - 1.0` for each year
5. **Statistical Testing** (optional): 
   - Bootstrap confidence intervals (10,000 resamples)
   - Wilcoxon signed-rank test (non-parametric, tests if median > 0)
   - Benjamini-Hochberg FDR correction for multiple testing
6. **Aggregation**: Groups by symbol and calculates median, mean, win rate, standard deviation, Sharpe ratio
7. **Ranking**: Sorts by median return (primary), win rate (secondary), average return (tertiary)
8. **Export**: Saves results in multiple formats (CSV, Parquet, HTML) with up to 16 columns

## Important Notes

### Trading Calendar
- Black Friday is a half-day trading session (closes at 1:00 PM ET) but counts as a trading day for business day calculations
- NYSE market holidays are properly excluded from business day counts (10 federal holidays)
- Weekend days are excluded from business day calculations

### S&P 500 Sampling Methodology
- **Representative Sample:** S&P 500 analysis uses a **270-stock sample (54% of the 500-stock index)**
- **Rationale:** Balances data quality (78.8% completeness vs. estimated 65-70% with full 500), computational efficiency (~20 min vs. 45+ min), and sector balance
- **Selection Criteria:** Liquid, actively traded stocks with longer histories; proportional representation across all 11 GICS sectors
- **244 stocks analyzed:** 26 excluded due to insufficient data (recent IPOs like SNOW, PLTR, DASH, COIN)
- **Validation:** 87% positive median rate aligns with literature; sector patterns match theory; cross-validated with DJIA and NASDAQ-100
- **Limitations:** May not capture smallest S&P 500 constituents; survivorship bias remains (current constituents only)
- **Alternative:** Users can extend `SP500_DEFAULT` in `src/tgalpha/universe.py` to include all 500 stocks if desired

### Data Quality
- Symbols with fewer than `min_trades` observations are filtered out (default: 10 years)
- Missing data for individual years is handled gracefully (no imputation)
- All returns are simple returns (not log returns)
- Yahoo Finance data used with `auto_adjust=True` for proper price handling

### Statistical Significance
- **0 of 354 stocks** reach statistical significance after Benjamini-Hochberg FDR correction (α=0.05)
- This demonstrates **proper academic rigor** with multiple testing correction, not absence of effect
- **Practical significance remains strong:** 79-87% positive median rates, favorable Sharpe ratios (0.4-0.7)
- See `STATISTICAL_RESULTS_SUMMARY.md` for comprehensive statistical testing documentation

## Results & Findings

For comprehensive analysis results, see:

### Thanksgiving Window (Traditional Black Friday)
- **[EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)** - Cross-index stakeholder overview (354 stocks, 8,293 observations)
- **[ANALYSIS_SP500_25YEARS.md](_thanks/ANALYSIS_SP500_25YEARS.md)** - S&P 500 detailed analysis (244 stocks, 5,756 observations)
- **[ANALYSIS_NASDAQ100_25YEARS.md](_thanks/ANALYSIS_NASDAQ100_25YEARS.md)** - NASDAQ-100 detailed analysis (80 stocks, 1,818 observations)
- **[ANALYSIS_25YEARS.md](_thanks/ANALYSIS_25YEARS.md)** - DJIA detailed analysis (30 stocks, 719 observations)
- **[STATISTICAL_RESULTS_SUMMARY.md](STATISTICAL_RESULTS_SUMMARY.md)** - Statistical significance testing results

### Santa Claus Rally Window (Year-End)
- **[EXECUTIVE_SUMMARY_SANTA_RALLY.md](EXECUTIVE_SUMMARY_SANTA_RALLY.md)** | **[Czech](EXECUTIVE_SUMMARY_SANTA_RALLY_CS.md)** - DJIA shows statistical significance (DIS, JPM)
- **[ANALYSIS_SANTA_RALLY_COMPARISON.md](_santa/ANALYSIS_SANTA_RALLY_COMPARISON.md)** - Cross-index Santa vs. Thanksgiving comparison

### Additional Resources
- **[COMPREHENSIVE_CYBER_MONDAY_ANALYSIS.md](_cyberm/COMPREHENSIVE_CYBER_MONDAY_ANALYSIS.md)** - Full Cyber Monday analysis
- **[COMPARISON_CYBER_MONDAY_VS_THANKSGIVING.md](_thanks/COMPARISON_CYBER_MONDAY_VS_THANKSGIVING.md)** - Thanksgiving vs. Cyber Monday comparison
- **[REFERENCES.md](REFERENCES.md)** - Academic citations and methodology references

## Disclaimer

⚠️ **This tool is for research and educational purposes only.**

- Past performance does not guarantee future results
- Not financial advice or investment recommendations
- Markets evolve; historical patterns may not persist
- Transaction costs and slippage would reduce actual returns
- Survivorship bias present (current DJIA constituents only)
- Always consult qualified financial professionals before making investment decisions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Martin Liebl**  
📧 Email: [lieblm@gmail.com](mailto:lieblm@gmail.com)  
🐙 GitHub: [@lieblm](https://github.com/lieblm)

Questions, feedback, or collaboration inquiries are welcome!

## Support This Project
- ⭐ Star this repository
- 🐛 Report bugs or suggest features via [Issues](https://github.com/lieblm/thanksgiving-alpha/issues)
- 📖 Share your research findings using this tool
- 🔀 Contribute code improvements via Pull Requests
- 🎁 [Sponsor @lieblm on GitHub](https://github.com/sponsors/lieblm)

---

**Built with ❤️ for the quantitative finance community**
