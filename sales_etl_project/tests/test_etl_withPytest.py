import pandas as pd
import pytest
from etl_sales import transform_data

@pytest.fixture
def sample_raw_df():
    return pd.DataFrame({
        "Region": ["East", "West", "East", None],
        "Date": ["2023-01-01", "2023-01-10", "2023-01-20", "2023-01-25"],
        "Sales": [1000, 2000, None, 1300]
    })

def test_transform_removes_nulls(sample_raw_df):
    result = transform_data(sample_raw_df)
    assert result.shape[0] == 2  # East and West (valid rows only)

def test_transform_has_expected_columns(sample_raw_df):
    result = transform_data(sample_raw_df)
    assert sorted(result.columns.tolist()) == sorted(["Region", "Month", "Sales"])

def test_month_format_is_correct(sample_raw_df):
    result = transform_data(sample_raw_df)
    assert all(result["Month"].str.match(r"^\d{4}-\d{2}$"))

def test_no_nulls_in_critical_columns(sample_raw_df):
    result = transform_data(sample_raw_df)
    assert not result["Region"].isnull().any()
    assert not result["Month"].isnull().any()
    assert not result["Sales"].isnull().any()

def test_sales_aggregation_correct(sample_raw_df):
    result = transform_data(sample_raw_df)
    east_sales = result[result["Region"] == "East"]["Sales"].values[0]
    west_sales = result[result["Region"] == "West"]["Sales"].values[0]
    assert east_sales == 1000  # Only valid East record
    assert west_sales == 2000
