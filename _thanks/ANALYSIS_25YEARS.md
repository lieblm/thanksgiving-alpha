# 25-Year Thanksgiving Seasonality Analysis
## DJIA Constituents: 2000-2024

**Analysis Period:** 2000-2024 (25 years)  
**Universe:** 30 DJIA Constituents (as of November 2025)  
**Trading Window:** 3 business days before Thanksgiving → 1 business day after (Black Friday, a half-day session closing at 1:00 PM ET)  
**Total Observations:** 718 stock-year combinations  
**Data Completeness:** 96% (718 out of 750 possible observations)  
**Filtering:** Minimum 10 observations required per stock

**Methodology:**
- **Return Calculation:** Simple returns (Close_after - Open_before) / Open_before
- **Trading Calendar:** NYSE business days excluding 10 federal holidays
- **Black Friday:** Counted as trading day (half-day session, 1:00 PM ET close)
- **Data Source:** Yahoo Finance via yfinance library (auto_adjust=True)
- **Statistical Tests:** See "Statistical Notes" section below

---

## Executive Highlights

### Top 10 Performers (by Median Return)

| Rank | Symbol | Company | Median Return | Avg Return | Win Rate | Years | Std Dev |
|------|--------|---------|---------------|------------|----------|-------|---------|
| 1 | AAPL | Apple | **+2.00%** | +1.79% | 68% | 25 | 4.03% |
| 2 | AMZN | Amazon | **+1.69%** | +2.11% | 76% | 25 | 4.50% |
| 3 | HD | Home Depot | **+1.26%** | +1.60% | 76% | 25 | 4.03% |
| 4 | UNH | UnitedHealth | **+1.21%** | +1.69% | 72% | 25 | 4.43% |
| 5 | NKE | Nike | **+1.14%** | +1.05% | 76% | 25 | 2.88% |
| 6 | VZ | Verizon | **+1.09%** | +1.43% | 64% | 25 | 3.28% |
| 7 | V | Visa | **+1.03%** | +0.89% | 59% | 17 | 3.23% |
| 8 | CSCO | Cisco | **+0.95%** | +0.72% | 56% | 25 | 2.76% |
| 9 | MCD | McDonald's | **+0.86%** | +0.91% | 72% | 25 | 2.01% |
| 10 | WMT | Walmart | **+0.84%** | +0.64% | 64% | 25 | 2.34% |

### Bottom 5 Performers

| Rank | Symbol | Company | Median Return | Avg Return | Win Rate | Years | Std Dev |
|------|--------|---------|---------------|------------|----------|-------|---------|
| 26 | GS | Goldman Sachs | **-0.04%** | +1.30% | 44% | 25 | 8.70% |
| 27 | JPM | JPMorgan Chase | **-0.13%** | +0.99% | 48% | 25 | 6.88% |
| 28 | JNJ | Johnson & Johnson | **-0.24%** | -0.40% | 32% | 25 | 1.35% |
| 29 | CRM | Salesforce | **-0.54%** | +0.87% | 38% | 21 | 7.22% |

---

## Key Insights

### 1. Technology Leadership
- **AAPL and AMZN** dominate with consistently positive median returns (>1.5%)
- **Technology sector** shows strongest Thanksgiving performance
- **MSFT** shows lower median (+0.44%) despite being a tech leader

### 2. Retail & Consumer
- **HD, NKE, WMT, MCD** all show positive median returns
- Likely benefiting from Black Friday retail anticipation (despite early 1:00 PM market close)
- **Consumer discretionary stocks** perform well in this window

### 3. Healthcare Strength
- **UNH** ranks 4th with +1.21% median return and 72% win rate
- Defensive characteristics provide stability

### 4. Financial Sector Weakness
- **GS and JPM** show negative median returns
- High volatility (std dev >6%)
- Lower win rates (44-48%)
- Financials appear to underperform during holiday period

### 5. Consistency Metrics
- **Highest Win Rates:** AMZN, HD, NKE (76% each)
- **Most Consistent:** MCD, PG (low volatility)
- **Highest Volatility:** GS (8.70%), CRM (7.22%), JPM (6.88%)

---

## Statistical Analysis

### Distribution of Returns

**Positive Median Returns:** 25 out of 30 stocks (83%)  
**Negative Median Returns:** 5 out of 30 stocks (17%)

### Win Rate Distribution
- **>70% Win Rate:** 6 stocks (AMZN, HD, UNH, NKE, MCD)
- **60-70% Win Rate:** 7 stocks
- **50-60% Win Rate:** 11 stocks
- **<50% Win Rate:** 6 stocks

### Volatility Tiers
- **Low Vol (<2.5%):** PG, JNJ, MCD, INTC, KO, MMM
- **Medium Vol (2.5-4%):** Most stocks (18 stocks)
- **High Vol (>6%):** GS, JPM, CRM

---

## Sector Performance Summary

| Sector | Top Performer | Median Return | Avg Win Rate |
|--------|---------------|---------------|--------------|
| Technology | AAPL (+2.00%) | +1.02% | 61% |
| Consumer Discretionary | AMZN (+1.69%) | +0.90% | 69% |
| Healthcare | UNH (+1.21%) | +0.52% | 60% |
| Consumer Staples | WMT (+0.84%) | +0.44% | 61% |
| Industrials | HON (+0.78%) | +0.45% | 63% |
| Energy | CVX (+0.49%) | +0.49% | 60% |
| Financials | AXP (+0.82%) | -0.08% | 46% |

---

## Risk-Return Profile

### Best Risk-Adjusted Returns (Sharpe-like)
1. **NKE:** +1.14% median / 2.88% std = 0.40 ratio
2. **AAPL:** +2.00% median / 4.03% std = 0.50 ratio
3. **MCD:** +0.86% median / 2.01% std = 0.43 ratio

### Highest Risk, Lowest Return
1. **GS:** -0.04% median / 8.70% std
2. **CRM:** -0.54% median / 7.22% std
3. **JPM:** -0.13% median / 6.88% std

---

## Data Quality Notes

### Missing Data
- **CRM (Salesforce):** Only 21 years (IPO: 2004)
- **V (Visa):** Only 17 years (IPO: 2008)
- **DOW:** Missing most years (recent DJIA addition)
- **BA (Boeing):** 24 years (1 timeout error)

### Survivorship Considerations
- Analysis uses **current DJIA constituents** (as of November 2025)
- Excludes companies that were removed from the index during 2000-2024 period
- This may introduce positive bias, though magnitude is difficult to quantify without historical constituent data
- Future analyses should consider point-in-time membership for unbiased estimates

### Data Completeness by Universe
- **DJIA:** 718 observations out of 750 possible (96% completeness)
- Highest completeness among the three indices analyzed (vs. S&P 500: 89%, NASDAQ-100: 79%)
- Mature, stable index membership contributes to excellent data coverage

---

## Returns Specification

**Important:** All returns reported in this analysis are **gross returns** (calculated from close-to-close prices without adjustments).

**Gross vs. Net Returns:**
- **Gross returns** = Price change only (Open → Close)
- **Net returns** = Gross returns minus transaction costs

**Transaction costs not included:**
- Bid-ask spreads (typically 0.01-0.05% for liquid DJIA stocks)
- Commissions (varies by broker, often zero for retail traders)
- Market impact for large orders (depends on position size)
- Slippage on market orders

**Implication:** Actual trading returns will be lower than reported gross returns. For small retail positions, the difference is typically minor (0.05-0.15%). For institutional size, costs can be more significant.

---

## Trading Implications

### Long Candidates (Positive Edge)
- **High Conviction:** AAPL, AMZN, HD (>1.5% median, >68% win rate)
- **Moderate Conviction:** UNH, NKE, VZ (1-1.5% median, >59% win rate)
- **Low Volatility:** MCD, NKE, WMT (stable, consistent)

### Avoid / Short Candidates
- **Negative Edge:** JNJ, JPM, GS, CRM (negative median returns)
- **High Volatility, Low Return:** GS, CRM (poor risk-reward)

### Portfolio Construction
- **Diversified Basket:** Top 10 stocks by median return
- **Risk Management:** Avoid high-volatility financials
- **Sector Tilt:** Overweight technology & consumer discretionary

---

## Comparison: 5-Year vs 25-Year Results

### Changes in Rankings

| Stock | 5-Yr Rank | 25-Yr Rank | Change |
|-------|-----------|------------|--------|
| BA | 1st | 14th | ↓ 13 |
| CVX | 2nd | 17th | ↓ 15 |
| VZ | 3rd | 6th | ↑ 3 |
| AAPL | - | 1st | New Top |
| AMZN | - | 2nd | New Top |

**Key Observation:** Short-term (5-year) leaders like BA and CVX show regression to the mean over longer periods. Technology stocks (AAPL, AMZN) demonstrate sustained outperformance over 25 years.

---

## Conclusions

1. **Thanksgiving Effect Exists:** 83% of stocks show positive median returns during the analysis window

2. **Technology Dominance:** Tech sector shows strongest and most consistent performance

3. **Retail Anticipation:** Consumer-facing stocks benefit from Black Friday retail expectations (despite half-day trading session closing at 1:00 PM ET)

4. **Financial Underperformance:** Banks and financial services show weakness during holiday period

5. **Statistical Robustness:** With 25 years of data and 718 observations across 30 stocks, empirical patterns show consistency over multiple economic cycles

6. **Risk Considerations:** 
   - Past performance doesn't guarantee future results
   - Each stock has maximum 25 observations (limited sample size for individual securities)
   - Survivorship bias present (current DJIA constituents only)
   - Gross returns reported; transaction costs will reduce actual net returns
   - Market conditions and participant behavior evolve over time
   - Holiday effect may diminish as more market participants become aware

---

## Academic Context

This analysis aligns with established literature on calendar anomalies and holiday effects in financial markets:

- **Lakonishok & Smidt (1988)** documented significant positive returns around major US holidays in their 90-year study
- **Ariel (1990)** specifically identified pre-holiday effects including Thanksgiving
- **Brockman & Michayluk (1998)** confirmed persistence of holiday effects through the 1990s

Our findings of 83% positive median returns during the Thanksgiving window are consistent with this academic literature, though readers should note that:
- Some calendar anomalies have diminished after publication (Market efficiency increases)
- Transaction costs and market impact can erode observed patterns
- Statistical significance testing with multiple hypothesis correction is essential

**For complete academic references and methodology, see:** [REFERENCES.md](../REFERENCES.md)

---

## Statistical Notes

**Methodology:**
- **Returns:** Simple returns (not log returns): (Close - Open) / Open
- **Median preferred over mean:** More robust to outliers
- **Win rate:** Percentage of years with positive returns
- **Standard deviation:** Annualized volatility proxy (though based on single observation per year)

**Statistical Significance:**
Future analyses should include:
- Bootstrap confidence intervals for median and mean returns
- Wilcoxon signed-rank test (non-parametric test vs. zero)
- Benjamini-Hochberg correction for multiple testing (30 stocks)
- Effect size measures (Cohen's d)
- Sharpe ratio calculations for risk-adjusted assessment

The enhanced analytical framework with these statistical tests is now available in the codebase (see `src/tgalpha/stats_tests.py`).

---

## Recommendations

**For Researchers:**
- Extend analysis to S&P 500 for broader validation ✅ **(COMPLETED - see ANALYSIS_SP500_25YEARS.md)**
- Test alternative windows (e.g., 5 days before/after, 2 days before/after)
- Analyze sector rotation patterns and factor exposures
- Implement statistical significance testing ✅ **(COMPLETED - see stats_tests.py module)**
- Consider point-in-time index membership to eliminate survivorship bias
- Compare holiday effect across different economic regimes (recession vs. expansion)

**For Traders:**
- **Long candidates (empirical edge):** AAPL, AMZN, HD, UNH, NKE
- **Avoid/short candidates:** JNJ, GS, JPM during this window
- Use appropriate position sizing and risk management
- Account for transaction costs in strategy design (bid-ask spreads, commissions, slippage)
- Consider that reported returns are gross; net returns will be lower
- Be aware of reduced liquidity on Black Friday half-day session (1:00 PM ET close)

**For Portfolio Managers:**
- Tactical tilt toward technology & consumer discretionary
- Reduce financial sector exposure around Thanksgiving
- Consider this as one factor among many in allocation decisions
- Backtest with realistic trading costs and market impact
- Monitor whether effect persists or diminishes over time
- Use statistical significance tests to validate any trading signals

---

## Appendix: Full Dataset

**Files Generated:**
- `data/outputs/ranking.csv` - Full results table (Excel-compatible)
- `data/outputs/ranking.parquet` - Compressed binary format (for big data analytics)
- `data/outputs/ranking.html` - Web-viewable formatted table

**Configuration Used:** `configs/djia_25years.yaml`

**Analysis Date:** November 6, 2025

**Command to Reproduce:**
```bash
python -m tgalpha.cli configs/djia_25years.yaml --top=30 --show-coverage
```

**Related Analyses:**
- [S&P 500 25-Year Analysis](ANALYSIS_SP500_25YEARS.md) - 264 stocks, 5,879 observations
- [NASDAQ-100 25-Year Analysis](ANALYSIS_NASDAQ100_25YEARS.md) - 96 stocks, 1,904 observations
- [Executive Summary](../EXECUTIVE_SUMMARY.md) - Cross-index synthesis with 8,501 total observations
- [Academic References](../REFERENCES.md) - 10 citations including Lakonishok & Smidt (1988)

---

**Disclaimer:** This analysis is for informational and research purposes only. It is not financial advice. All returns reported are gross returns that do not account for transaction costs, taxes, or other real-world trading expenses. Past performance does not guarantee future results. Trading and investing involve risk of loss. Consult with a qualified financial advisor before making investment decisions. The authors make no representations about the accuracy or completeness of this analysis and disclaim all liability for any losses arising from reliance on this information.
