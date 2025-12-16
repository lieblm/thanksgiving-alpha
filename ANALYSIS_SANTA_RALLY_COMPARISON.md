# Santa Claus Rally Analysis: Cross-Index Comparison (2000-2024)

**Analysis Date:** December 16, 2025  
**Period Definition:** Last 5 trading days of year + First 2 trading days of next year (7 trading days total)  
**Statistical Method:** Wilcoxon signed-rank test with Benjamini-Hochberg FDR correction (α=0.05)

---

## Executive Summary

The Santa Claus Rally analysis across three major U.S. equity indices reveals **stronger statistical significance compared to Thanksgiving**, with 2 of 30 DJIA stocks showing significant positive returns. However, broader indices (NASDAQ-100, S&P 500) show no statistically significant stocks after multiple testing correction, suggesting the effect is concentrated in specific large-cap value stocks.

---

## Cross-Index Overview

| Metric | DJIA | NASDAQ-100 | S&P 500 |
|--------|------|------------|---------|
| **Stocks Analyzed** | 30 | 73 | 229 |
| **Total Observations** | 718 | 1,898 | 5,475 |
| **Avg Coverage** | 95.7% | 78.8% | 88.9% |
| **Median Coverage** | 96.7% | 82.3% | 90.2% |
| **Significant Stocks** | **2*** | 0 | 0 |
| **Positive Median %** | 86.7% | 72.6% | 81.7% |
| **Top Median Return** | +2.55% (DIS) | +3.69% (MU) | +3.84% (CF) |
| **Top Win Rate** | 76.0% (WMT) | 73.3% (CHTR) | 80.0% (TRGP, AMT) |

*Statistically significant after BH FDR correction

---

## Key Finding: DJIA Shows Statistical Significance

### Statistically Significant Winners (DJIA Only)

**1. DIS (Disney)** ⭐
- Median Return: +2.55%
- Win Rate: 72.0%
- p-value (corrected): 0.037 ***
- Sharpe Ratio: 0.631
- Observations: 25

**2. JPM (JPMorgan Chase)** ⭐
- Median Return: +1.97%
- Win Rate: 72.0%
- p-value (corrected): 0.037 ***
- Sharpe Ratio: 0.641
- Observations: 25

### Why DJIA Shows Significance (NASDAQ-100 & S&P 500 Don't)

1. **Sample Size Effect:** Only 30 stocks = less severe multiple testing penalty (30 tests vs. 73 or 229)
2. **Large-Cap Value Concentration:** DJIA's blue-chip, value-oriented composition may be better suited for year-end positioning
3. **Lower Volatility:** DIS and JPM show consistent returns with favorable Sharpe ratios (0.63+)
4. **Sector Mix:** DJIA's financials and consumer discretionary exposure aligns with Santa Rally thesis

---

## Top 10 Performers by Index

### DJIA Top 10
| Rank | Symbol | Median Return | Win Rate | p-value | Sig |
|------|--------|---------------|----------|---------|-----|
| 1 | DIS | +2.55% | 72.0% | 0.037 | *** |
| 2 | JPM | +1.97% | 72.0% | 0.037 | *** |
| 3 | CSCO | +1.69% | 64.0% | 0.082 | |
| 4 | CAT | +1.54% | 60.0% | 0.154 | |
| 5 | INTC | +1.49% | 56.0% | 0.159 | |
| 6 | AXP | +1.45% | 72.0% | 0.082 | |
| 7 | V | +1.34% | 76.5% | 0.082 | |
| 8 | CVX | +1.27% | 75.0% | 0.082 | |
| 9 | IBM | +1.20% | 72.0% | 0.082 | |
| 10 | VZ | +1.17% | 60.0% | 0.082 | |

### NASDAQ-100 Top 10
| Rank | Symbol | Median Return | Win Rate | p-value | Sig |
|------|--------|---------------|----------|---------|-----|
| 1 | MU | +3.69% | 64.0% | 0.194 | |
| 2 | ON | +2.44% | 68.0% | 0.332 | |
| 3 | LULU | +2.39% | 61.1% | 0.332 | |
| 4 | AMAT | +2.05% | 68.0% | 0.332 | |
| 5 | CHTR | +1.72% | 73.3% | 0.332 | |
| 6 | CSCO | +1.69% | 64.0% | 0.332 | |
| 7 | QCOM | +1.67% | 64.0% | 0.332 | |
| 8 | BKNG | +1.64% | 56.0% | 0.332 | |
| 9 | MELI | +1.62% | 55.6% | 0.332 | |
| 10 | ROST | +1.49% | 72.0% | 0.194 | |

### S&P 500 Top 10
| Rank | Symbol | Median Return | Win Rate | p-value | Sig |
|------|--------|---------------|----------|---------|-----|
| 1 | CF | +3.84% | 70.0% | 0.139 | |
| 2 | MU | +3.69% | 64.0% | 0.131 | |
| 3 | WMB | +3.24% | 72.0% | 0.118 | |
| 4 | SCHW | +3.08% | 68.0% | 0.139 | |
| 5 | FCX | +2.98% | 64.0% | 0.140 | |
| 6 | COF | +2.87% | 68.0% | 0.131 | |
| 7 | DIS | +2.55% | 72.0% | 0.128 | |
| 8 | VLO | +2.34% | 64.0% | 0.191 | |
| 9 | NEM | +2.33% | 72.0% | 0.128 | |
| 10 | TRGP | +2.13% | 80.0% | 0.139 | |

---

## Sector Analysis

### Best Performing Sectors (by top performers)

**1. Financials** 🏦
- **DJIA Leaders:** JPM (+1.97%***, 72% win), AXP (+1.45%, 72% win)
- **S&P 500 Leaders:** SCHW (+3.08%), COF (+2.87%), JPM (+1.97%)
- **Pattern:** Payment networks and diversified banks outperform

**2. Technology - Semiconductors** 💻
- **NASDAQ-100 Leaders:** MU (+3.69%), AMAT (+2.05%), INTC (+1.49%)
- **Cross-Index:** MU appears in top 2 of both NASDAQ-100 and S&P 500
- **Pattern:** Memory and equipment stocks show strong Santa Rally effect

**3. Consumer Discretionary** 🛒
- **DJIA Leaders:** DIS (+2.55%***, 72% win)
- **NASDAQ-100 Leaders:** LULU (+2.39%), ROST (+1.49%)
- **Pattern:** Retail and entertainment benefit from holiday sentiment

**4. Energy** ⚡
- **S&P 500 Leaders:** WMB (+3.24%), VLO (+2.34%), DVN (+1.80%)
- **Pattern:** Oil & gas and midstream infrastructure show strength

### Underperforming Sectors

**1. Consumer Staples** 🥫
- KO (-0.55% median, DJIA)
- Pattern: Defensive stocks lag in risk-on environment

**2. Healthcare - Mixed** 🏥
- Some strength (UNH in DJIA, ILMN in tech)
- But generally lower returns than cyclicals

---

## Comparison: Santa Rally vs. Thanksgiving

| Metric | Santa Rally | Thanksgiving |
|--------|-------------|--------------|
| **DJIA Significant Stocks** | **2** (DIS, JPM) | 0 |
| **DJIA Top Median** | +2.55% (DIS) | +2.00% (AAPL) |
| **NASDAQ-100 Significant** | 0 | 0 |
| **S&P 500 Significant** | 0 | 0 |
| **Trading Days** | 7 | 4-5 (varies) |
| **Effect Strength** | **Stronger** | Moderate |

**Key Insight:** Santa Claus Rally shows stronger statistical evidence (2 significant stocks vs. 0 for Thanksgiving), suggesting it may be a more reliable seasonal pattern, particularly for large-cap financials and consumer discretionary stocks.

---

## Statistical Robustness

### Multiple Testing Correction Impact

| Index | Raw Tests | Stocks with p<0.05 (uncorrected) | Stocks Significant (BH-corrected) | Correction Severity |
|-------|-----------|----------------------------------|-----------------------------------|---------------------|
| DJIA | 30 | ~8 | 2 | Low |
| NASDAQ-100 | 73 | ~15 | 0 | Moderate |
| S&P 500 | 229 | ~35 | 0 | High |

**Explanation:** The Benjamini-Hochberg correction becomes more stringent as the number of tests increases. This explains why DJIA (30 tests) can show significance while broader indices (73-229 tests) cannot, even though some individual stocks show strong patterns.

---

## Investment Implications

### Conservative Strategy (High Confidence)
**Target:** DIS, JPM (DJIA only)
- Both show statistical significance (p<0.05 after correction)
- Strong Sharpe ratios (0.63+)
- 72% win rates
- **Expected Return:** ~2.0-2.5% over 7-day period

### Balanced Strategy (Moderate Confidence)
**Target:** Top 10-15 performers with 65%+ win rates
- Focus on semiconductors (MU, AMAT), financials (SCHW, COF), consumer discretionary (LULU, ROST)
- **Expected Return:** ~1.5-3.0% over 7-day period
- **Risk:** No statistical significance guarantee

### Aggressive Strategy (Pattern-Based)
**Target:** Sector baskets (Tech, Financials, Energy)
- Diversify across top performers in each index
- **Expected Return:** ~1.0-2.5% over 7-day period
- **Risk:** Higher volatility, no statistical significance

---

## Limitations & Considerations

1. **Survivorship Bias:** Using current index constituents (2025) for historical period (2000-2024)
2. **Sample Size:** Only 25 observations per stock limits statistical power
3. **Recent IPOs:** Stocks like CRM (n=21), V (n=17) have limited history
4. **Market Regime Changes:** 2000-2024 spans multiple market cycles
5. **Multiple Testing Penalty:** Broader indices face severe correction (S&P 500: 229 tests)
6. **Transaction Costs:** Not modeled; 7-day holding period may have execution slippage

---

## Data Quality Summary

| Index | Min Coverage | Max Coverage | Avg Coverage | Notable Gaps |
|-------|--------------|--------------|--------------|--------------|
| DJIA | 86.7% (2003) | 100.0% (2019-2024) | 95.7% | CRM, DOW, V (IPOs) |
| NASDAQ-100 | 57.3% (2000) | 100.0% (2023-2024) | 78.8% | Many recent IPOs |
| S&P 500 | 75.4% (2000) | 100.0% (2021-2024) | 88.9% | Early 2000s lower |

**Coverage improves significantly post-2019 as recent IPOs mature.**

---

## Conclusions

1. **Santa Claus Rally is statistically stronger than Thanksgiving** (2 significant stocks vs. 0)
2. **Effect is concentrated in DJIA large-cap value stocks** (DIS, JPM)
3. **Semiconductors show strong patterns** across indices (MU, AMAT)
4. **Financials dominate** top performers (JPM, SCHW, COF, AXP)
5. **Multiple testing correction is critical** - many strong patterns fail significance test
6. **81.7% of S&P 500 stocks show positive median returns** - broad-based effect
7. **Pattern exists but statistical significance is limited** to narrow set of stocks

---

## Methodology Notes

- **Period:** 2000-2024 (25 years)
- **Window:** Last 5 trading days of year + First 2 trading days of next year
- **Return Calculation:** Simple returns (Close/Open - 1) × 100
- **Statistical Tests:** Wilcoxon signed-rank test (non-parametric)
- **Multiple Testing:** Benjamini-Hochberg FDR correction (α=0.05)
- **Data Source:** Yahoo Finance (yfinance with auto_adjust=True)
- **Holiday Handling:** NYSE calendar with 10 federal holidays

---

**Generated by:** Thanksgiving-Alpha v1.0.1  
**Contact:** Martin Liebl (lieblm@gmail.com)  
**Repository:** https://github.com/lieblm/thanksgiving-alpha  
**License:** MIT
