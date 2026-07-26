"""
Central in-memory data store for the Smart Facility Management API.

The source dataset ships as a multi-sheet Excel workbook. On startup we load
every sheet into a pandas DataFrame, normalize dtypes (dates/timestamps), and
keep everything in memory. With only ~200 rows per sheet this is fast and
avoids standing up a separate database just for a demo dataset -- swap
`load_all()` for a real DB layer (Postgres, etc.) if this grows beyond a demo.
"""
from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "facility_data.xlsx"


class Store:
    """Holds every sheet as a DataFrame, keyed by sheet name."""

    def __init__(self):
        self.tables: dict[str, pd.DataFrame] = {}

    def load_all(self):
        xl = pd.ExcelFile(DATA_FILE)
        for sheet in xl.sheet_names:
            self.tables[sheet] = xl.parse(sheet)
        self._normalize()
        return self

    def _normalize(self):
        t = self.tables

        t["energy_usage"]["timestamp"] = pd.to_datetime(t["energy_usage"]["timestamp"])
        t["occupancy"]["timestamp"] = pd.to_datetime(t["occupancy"]["timestamp"])
        t["security_events"]["event_time"] = pd.to_datetime(t["security_events"]["event_time"])
        t["alerts"]["created_at"] = pd.to_datetime(t["alerts"]["created_at"])
        t["maintenance_records"]["maintenance_date"] = pd.to_datetime(
            t["maintenance_records"]["maintenance_date"]
        )
        t["assets"]["install_date"] = pd.to_datetime(t["assets"]["install_date"])
        # "month" is stored like "Feb-2026" -- keep the label but add a sortable period
        t["cost_reports"]["month_period"] = pd.to_datetime(
            t["cost_reports"]["month"], format="%b-%Y"
        )

        # Maintenance records only carry asset_id -- join in facility_id so callers
        # can filter maintenance by facility without re-deriving this every request.
        asset_facility = t["assets"][["asset_id", "facility_id"]]
        t["maintenance_records"] = t["maintenance_records"].merge(
            asset_facility, on="asset_id", how="left"
        )

    def df(self, name: str) -> pd.DataFrame:
        return self.tables[name].copy()


store = Store()


def get_store() -> Store:
    return store
