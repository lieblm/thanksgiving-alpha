from pydantic import BaseModel
from typing import List, Literal


class Window(BaseModel):
    days_before: int = 3
    days_after: int = 1
    include_open_before: bool = True
    include_close_after: bool = True


class Session(BaseModel):
    market: Literal["US"] = "US"
    timezone: str = "America/New_York"
    respect_half_days: bool = True
    data_source: Literal["yahoo"] = "yahoo"


class Filters(BaseModel):
    min_history_years: int = 10
    exclude_missing_ratio: float = 0.05


class Ranking(BaseModel):
    sort_by: List[str] = ["median_return", "win_rate", "avg_return"]
    min_trades: int = 10


class OutputCfg(BaseModel):
    dir: str = "data/outputs"
    formats: List[str] = ["parquet", "csv", "html"]


class CacheCfg(BaseModel):
    enabled: bool = True
    dir: str = "data/cache"


class Config(BaseModel):
    universe: str
    index_symbols: List[str] = []
    start_year: int
    end_year: int
    holiday: Literal["US_THANKSGIVING", "SANTA_CLAUS_RALLY"] = "US_THANKSGIVING"
    window: Window = Window()
    session: Session = Session()
    filters: Filters = Filters()
    ranking: Ranking = Ranking()
    output: OutputCfg = OutputCfg()
    cache: CacheCfg = CacheCfg()
