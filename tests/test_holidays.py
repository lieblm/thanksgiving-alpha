from datetime import date
from tgalpha.holidays import thanksgiving, santa_claus_rally_period


def test_thanksgiving_2025() -> None:
    assert str(thanksgiving(2025)) == "2025-11-27"


def test_thanksgiving_2024() -> None:
    """Test that Thanksgiving 2024 is correctly calculated."""
    assert str(thanksgiving(2024)) == "2024-11-28"


def test_thanksgiving_2023() -> None:
    """Test that Thanksgiving 2023 is correctly calculated."""
    assert str(thanksgiving(2023)) == "2023-11-23"


def test_thanksgiving_1990() -> None:
    """Test that Thanksgiving 1990 is correctly calculated."""
    assert str(thanksgiving(1990)) == "1990-11-22"


def test_thanksgiving_is_thursday() -> None:
    """Test that Thanksgiving is always a Thursday."""
    for year in range(1990, 2026):
        tg = thanksgiving(year)
        # Thursday is weekday 3 in Python's date.weekday()
        assert tg.weekday() == 3, f"Thanksgiving {year} ({tg}) is not a Thursday"


def test_thanksgiving_is_fourth_thursday() -> None:
    """Test that Thanksgiving is the 4th Thursday of November."""
    for year in range(1990, 2026):
        tg = thanksgiving(year)
        # Count Thursdays before this date in November
        thursdays_before = 0
        for day in range(1, tg.day):
            if date(year, 11, day).weekday() == 3:
                thursdays_before += 1
        # This should be the 4th Thursday (0-indexed: 3)
        assert thursdays_before == 3, f"Thanksgiving {year} is not the 4th Thursday"


def test_santa_claus_rally_2024() -> None:
    """Test Santa Claus Rally period for 2024."""
    start, end = santa_claus_rally_period(2024)
    assert start == date(2024, 12, 24)
    assert end == date(2025, 1, 3)


def test_santa_claus_rally_2023() -> None:
    """Test Santa Claus Rally period for 2023."""
    start, end = santa_claus_rally_period(2023)
    assert start == date(2023, 12, 24)
    assert end == date(2024, 1, 3)


def test_santa_claus_rally_spans_year_boundary() -> None:
    """Test that Santa Claus Rally period spans year boundary."""
    for year in range(2000, 2026):
        start, end = santa_claus_rally_period(year)
        assert start.year == year, f"Start date should be in {year}"
        assert end.year == year + 1, f"End date should be in {year + 1}"


def test_santa_claus_rally_period_length() -> None:
    """Test that Santa Claus Rally period has reasonable length."""
    for year in range(2000, 2026):
        start, end = santa_claus_rally_period(year)
        days_diff = (end - start).days
        # Should be approximately 10 days (Dec 24 to Jan 3)
        assert days_diff == 10, f"Period length for {year} should be 10 days, got {days_diff}"
