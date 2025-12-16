from datetime import date
import polars as pl
import pandas as pd
from typing import Tuple, Optional, Literal

from .holidays import thanksgiving
from .calendar_utils import us_trading_calendar, shift_business_days


def holiday_window_dates(
    year: int,
    x_before: int,
    y_after: int,
    holiday_type: Literal["US_THANKSGIVING", "SANTA_CLAUS_RALLY"] = "US_THANKSGIVING",
) -> Tuple[pd.Timestamp, pd.Timestamp]:
    """Calculate the trading window around a holiday for a given year.

    Args:
        year: The year to calculate for
        x_before: Number of business days before the holiday anchor
        y_after: Number of business days after the holiday anchor
        holiday_type: Type of holiday ("US_THANKSGIVING" or "SANTA_CLAUS_RALLY")

    Returns:
        Tuple of (open_date, close_date) as pd.Timestamps
    """
    if holiday_type == "SANTA_CLAUS_RALLY":
        # For Santa Claus Rally, we need a calendar that spans year boundary
        # Last 5 trading days of year + first 2 trading days of next year
        # Build calendar from Dec to Jan of next year
        cal = us_trading_calendar(date(year, 12, 1), date(year + 1, 1, 31))

        # Get the last trading day of the year
        # Find last trading day by going backward from Jan 1 of next year
        year_end_anchor = date(year + 1, 1, 1)
        last_trading_day = shift_business_days(cal, year_end_anchor, -1)

        # Go back 4 more trading days (5 total including last day)
        before = shift_business_days(cal, last_trading_day.date(), -4)

        # Get first trading day of next year by going forward from Jan 1
        first_trading_day = shift_business_days(cal, year_end_anchor, 1)

        # Go forward 1 more trading day (2 total including first day)
        after = shift_business_days(cal, first_trading_day.date(), 1)

        return before, after
    else:
        # US_THANKSGIVING logic
        h = thanksgiving(year)
        # Build calendar for the full year to ensure we have enough buffer
        cal = us_trading_calendar(date(year, 1, 1), date(year, 12, 31))
        before = shift_business_days(cal, h, -x_before)
        after = shift_business_days(cal, h, y_after)
        return before, after


def compute_return(
    df: pl.DataFrame, open_day: pd.Timestamp, close_day: pd.Timestamp
) -> Optional[float]:
    """Compute the return from open price on open_day to close price on close_day.

    Args:
        df: DataFrame with columns Date, Open, Close
        open_day: Date to take the Open price from
        close_day: Date to take the Close price from

    Returns:
        The return (close/open - 1.0) or None if data is missing
    """
    try:
        open_date = open_day.to_pydatetime()
        close_date = close_day.to_pydatetime()

        open_row = df.filter(pl.col("Date") == open_date)
        close_row = df.filter(pl.col("Date") == close_date)

        if open_row.is_empty() or close_row.is_empty():
            return None

        o = open_row["Open"].item()
        c = close_row["Close"].item()

        if o is None or c is None or o <= 0:
            return None

        return float(c / o - 1.0)
    except Exception:
        return None
