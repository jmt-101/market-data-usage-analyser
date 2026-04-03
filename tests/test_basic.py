import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/mock_usage_file.csv")

def test_file_exists():
    assert DATA_PATH.exists(), "usage_log.csv is missing"

def test_loads_correctly():
    df = pd.read_csv(DATA_PATH)
    assert len(df) > 0, "Dataset should not be empty"

def test_required_columns():
    df = pd.read_csv(DATA_PATH)
    required = {"timestamp", "user_id", "service", "ric", "msg_count", "bytes", "entitlement"}
    assert required.issubset(df.columns), "Missing required columns"

def test_basic_aggregation():
    df = pd.read_csv(DATA_PATH)
    grouped = df.groupby("user_id")["msg_count"].sum()
    assert grouped is not None