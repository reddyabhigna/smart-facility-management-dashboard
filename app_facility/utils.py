"""Small shared helpers used across routers."""
import pandas as pd


def to_records(df: pd.DataFrame) -> list[dict]:
    """Convert a DataFrame to JSON-safe list[dict].

    Handles Timestamp -> ISO string and NaN/NaT -> None, which FastAPI's
    default jsonable_encoder does not do cleanly for pandas objects.
    """
    df = df.copy()
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.strftime("%Y-%m-%dT%H:%M:%S")
    return df.where(pd.notnull(df), None).to_dict(orient="records")


def apply_filter(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    """Filter a DataFrame by an optional query param -- no-op when value is None."""
    if value is None:
        return df
    return df[df[column] == value]


def apply_date_range(df: pd.DataFrame, column: str, start, end) -> pd.DataFrame:
    if start is not None:
        df = df[df[column] >= pd.to_datetime(start)]
    if end is not None:
        df = df[df[column] <= pd.to_datetime(end)]
    return df
