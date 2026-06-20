import polars as pl
import pytest

from opendata.mhlw.covid_19 import (
    PCR_CSV_METADATA,
    PCR_RENAMED_HEADER,
    POSITIVE_CSV_METADATA,
    POSITIVE_RENAMED_HEADER,
)
from utils import csv_util


def test_pcr_metadata_has_required_keys():
    assert "target_url_list" in PCR_CSV_METADATA
    assert "header" in PCR_CSV_METADATA
    assert "dropna" in PCR_CSV_METADATA


def test_pcr_rename_maps_columns_correctly():
    raw = pl.DataFrame({
        "日付": ["2020-01-01", "2020-01-02"],
        "PCR 検査実施人数(単日)": ["100", "200"],
    })
    result = raw.rename(PCR_RENAMED_HEADER)
    assert "date" in result.columns
    assert "tests" in result.columns


def test_pcr_fill_null_replaces_missing_values():
    # Polars infers numeric columns from CSV as Int64/Float64, not String
    raw = pl.DataFrame({
        "日付": ["2020-01-01", "2020-01-02"],
        "PCR 検査実施人数(単日)": pl.Series([100, None], dtype=pl.Int64),
    })
    result = raw.rename(PCR_RENAMED_HEADER).fill_null(0).with_columns(pl.col("tests").cast(pl.Int64))
    assert result["tests"].to_list() == [100, 0]


def test_positive_rename_maps_columns_correctly():
    raw = pl.DataFrame({"Date": ["2020-01-01"], "ALL": ["50"]})
    result = raw.rename(POSITIVE_RENAMED_HEADER)
    assert "date" in result.columns
    assert "positives" in result.columns


def test_positive_cast_to_int():
    raw = pl.DataFrame({"Date": ["2020-01-01"], "ALL": ["50"]})
    result = raw.rename(POSITIVE_RENAMED_HEADER).with_columns(pl.col("positives").cast(pl.Int64))
    assert result["positives"].dtype == pl.Int64


def test_join_pcr_and_positive():
    pcr = pl.DataFrame({"date": ["2020-01-01", "2020-01-02"], "tests": [100, 200]})
    positive = pl.DataFrame({"date": ["2020-01-01"], "positives": [10]})
    result = csv_util.join_csv(pcr, "left", positive, "date")
    assert result.shape[0] == 2
    assert result.filter(pl.col("date") == "2020-01-01")["positives"][0] == 10
