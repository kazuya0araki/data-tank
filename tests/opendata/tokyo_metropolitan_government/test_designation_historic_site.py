import polars as pl
import pytest

from opendata.tokyo_metropolitan_government.designation_historic_site import CSV_METADATA
from utils import csv_util


def test_metadata_has_required_keys():
    assert "target_url_list" in CSV_METADATA
    assert "header" in CSV_METADATA
    assert "dropna" in CSV_METADATA


def test_metadata_dropna_columns_are_in_header():
    for col in CSV_METADATA["dropna"]:
        assert col in CSV_METADATA["header"]


def test_strip_removes_whitespace_from_name():
    data = pl.DataFrame({"名称": ["  東京タワー  ", "浅草寺 ", " 明治神宮"]})
    result = data.with_columns(csv_util.strip(data, "名称").alias("名称"))
    assert result["名称"].to_list() == ["東京タワー", "浅草寺", "明治神宮"]


def test_distinct_removes_duplicate_rows():
    data = pl.DataFrame({
        "名称": ["東京タワー", "浅草寺", "東京タワー"],
        "住所": ["港区", "台東区", "港区"],
    })
    result = csv_util.distinct(data)
    assert result.shape[0] == 2
