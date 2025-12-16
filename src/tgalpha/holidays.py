from datetime import date
import pandas as pd
from typing import cast, Tuple


def thanksgiving(year: int) -> date:
    """Calculate the date of US Thanksgiving for a given year.

    US Thanksgiving is the 4th Thursday of November.

    Args:
        year: The year to calculate Thanksgiving for

    Returns:
        The date of Thanksgiving
    """
    # Start from November 1st
    d = pd.Timestamp(year=year, month=11, day=1)

    # Find all Thursdays in November
    thursdays = [
        d + pd.Timedelta(days=i)
        for i in range(30)
        if (d + pd.Timedelta(days=i)).weekday() == 3  # Thursday = 3
    ]

    # Return the 4th Thursday (0-indexed: index 3)
    return cast(date, thursdays[3].date())


def santa_claus_rally_period(year: int) -> Tuple[date, date]:
    """Calculate the Santa Claus Rally period for a given year.

    The Santa Claus Rally period is defined as the last 5 trading days
    of the year and the first 2 trading days of the next year.
    
    Note: This function returns calendar dates, not trading days.
    The actual trading day calculation must account for weekends and holidays
    using the calendar_utils module.

    Args:
        year: The year to calculate the Santa Claus Rally period for

    Returns:
        Tuple of (start_date, end_date) representing the approximate period.
        Start date is December 24th of the given year.
        End date is January 3rd of the next year.
        These dates provide a buffer for the actual last 5 + first 2 trading days.
    """
    # Return a date range that encompasses the last 5 trading days of year
    # and first 2 trading days of next year
    # Using Dec 24 - Jan 3 gives enough buffer for holidays/weekends
    start_date = date(year, 12, 24)
    end_date = date(year + 1, 1, 3)
    
    return start_date, end_date
