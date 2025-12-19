# Santa Claus Rally: Executive Summary

*Statistically significant after Benjamini-Hochberg FDR correction (α=0.05)*

---

## Statistically Significant Winners

### DIS (Walt Disney) ⭐
- **Median Return:** +2.55%
- **Win Rate:** 72% (18 of 25 years)
- **p-value:** 0.037 (significant after correction)
- **Sharpe Ratio:** 0.631
- **Sector:** Consumer Discretionary

### JPM (JPMorgan Chase) ⭐
- **Median Return:** +1.97%
- **Win Rate:** 72% (18 of 25 years)
- **p-value:** 0.037 (significant after correction)
- **Sharpe Ratio:** 0.641
- **Sector:** Financials

**Key Finding:** These are the **only two stocks** across all three indices that pass rigorous statistical testing with multiple testing correction.

---

## Pattern Strength by Index

**Positive Median Returns:**
- DJIA: 86.7% (26 of 30 stocks)
- NASDAQ-100: 72.6% (53 of 73 stocks)
- S&P 500: 81.7% (187 of 229 stocks)

**Broad-Based Effect:** Over 80% of stocks show positive median returns in DJIA and S&P 500, suggesting widespread year-end optimism, but concentrated statistical significance.

---

## Top 5 Performers by Index

### DJIA Top 5
1. **DIS** +2.55% (72% win, p=0.037***)
2. **JPM** +1.97% (72% win, p=0.037***)
3. CSCO +1.69% (64% win)
4. CAT +1.54% (60% win)
5. INTC +1.49% (56% win)

### NASDAQ-100 Top 5
1. MU +3.69% (64% win)
2. ON +2.44% (68% win)
3. LULU +2.39% (61% win)
4. AMAT +2.05% (68% win)
5. CHTR +1.72% (73% win)

### S&P 500 Top 5
1. CF +3.84% (70% win)
2. MU +3.69% (64% win)
3. WMB +3.24% (72% win)
4. SCHW +3.08% (68% win)
5. FCX +2.98% (64% win)

---

## Sector Winners

**1. Financials** 🏦
- JPM, SCHW, COF, AXP all in top performers
- Payment networks and diversified banks dominate
- Year-end portfolio rebalancing drives demand

**2. Semiconductors** 💻
- MU, AMAT, INTC show strong patterns
- Memory and equipment stocks benefit
- Tech sector optimism for next year

**3. Consumer Discretionary** 🛒
- DIS (statistically significant), LULU, ROST
- Holiday sentiment and retail strength
- Entertainment and specialty retail lead

**4. Energy** ⚡
- WMB, VLO, FCX, DVN in S&P 500 top 10
- Commodity exposure and year-end positioning

---

## Why DJIA Shows Significance (Others Don't)

1. **Multiple Testing Penalty:** DJIA tests 30 stocks vs. 73 (NASDAQ) or 229 (S&P), making statistical significance easier to achieve
2. **Sample Composition:** Large-cap value stocks more suitable for year-end positioning
3. **Sector Mix:** DJIA's financials and consumer discretionary align with Santa Rally thesis
4. **Lower Volatility:** DIS and JPM show consistent returns with favorable risk profiles

---

## Investment Strategies

### Conservative (Highest Confidence)
**Target:** DIS, JPM only
- Both statistically significant (p<0.05 after correction)
- Expected return: ~2.0-2.5% over 7 days
- Win rate: 72%
- **Best for:** Risk-averse investors seeking evidence-based positions

### Balanced (Moderate Confidence)
**Target:** Top 10-15 performers with 65%+ win rates
- Semiconductors: MU, AMAT
- Financials: SCHW, COF, AXP
- Consumer: LULU, ROST
- Expected return: ~1.5-3.0% over 7 days
- **Best for:** Active traders with sector diversification

### Aggressive (Pattern-Based)
**Target:** Sector baskets (Tech, Financials, Energy)
- Diversified exposure across top performers
- Expected return: ~1.0-2.5% over 7 days
- Higher volatility, no statistical guarantee
- **Best for:** Speculation on seasonal pattern

---

## Comparison: Santa Rally vs. Thanksgiving

| Metric | Santa Rally | Thanksgiving |
|--------|-------------|--------------|
| Trading Days | 7 | 4-5 |
| DJIA Significant Stocks | **2** | 0 |
| DJIA Top Return | +2.55% (DIS) | +2.00% (AAPL) |
| DJIA Positive % | 86.7% | 83.3% |
| Effect Strength | **Stronger** | Moderate |

**Verdict:** Santa Claus Rally provides stronger statistical evidence and may be more reliable for systematic trading strategies.

---

## Methodology

- **Statistical Test:** Wilcoxon signed-rank test (non-parametric)
- **Multiple Testing Correction:** Benjamini-Hochberg FDR (α=0.05)
- **Sample Size:** 25 observations per stock (2000-2024)
- **Return Calculation:** Simple returns (Close/Open - 1) × 100
- **Data Source:** Yahoo Finance with auto-adjustment
- **Holiday Calendar:** NYSE with 10 federal holidays

---

## Limitations

1. **Survivorship Bias:** Current index constituents used for historical period
2. **Sample Size:** 25 years provides limited statistical power
3. **Multiple Testing:** Severe penalty for broader indices (S&P 500: 229 tests)
4. **Transaction Costs:** Not modeled; may reduce realized returns
5. **Market Regime:** 2000-2024 spans multiple cycles (tech bubble, financial crisis, COVID)

---

## Key Takeaways

✅ **Santa Claus Rally is statistically validated** in 2 DJIA stocks (vs. 0 for Thanksgiving)  
✅ **Broad-based positive pattern** (81.7% of S&P 500 stocks have positive median)  
✅ **Financials and consumer discretionary lead** with statistical significance  
✅ **Semiconductors show strong patterns** across all indices  
✅ **7-day window provides clear entry/exit** for tactical positioning  
⚠️ **Statistical significance is rare** after proper multiple testing correction  
⚠️ **No guarantee of future performance** despite historical patterns  

---

## For More Information

- **Full Analysis:** [ANALYSIS_SANTA_RALLY_COMPARISON.md](_santa/ANALYSIS_SANTA_RALLY_COMPARISON.md)
- **Repository:** https://github.com/lieblm/thanksgiving-alpha
- **Methodology:** [README.md](https://github.com/lieblm/thanksgiving-alpha/blob/main/README.md) for technical details
- **Citation:** [CITATION.cff](https://github.com/lieblm/thanksgiving-alpha/blob/main/CITATION.cff) for academic use

---

**Disclaimer:** This analysis is for educational and research purposes only. Past performance does not guarantee future results. No investment advice is provided. Always consult a financial advisor before making investment decisions.

---

**Contact:** Martin Liebl (lieblm@gmail.com)  
**License:** MIT  
**Version:** 1.0 (December 2025)
