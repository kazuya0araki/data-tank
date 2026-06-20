import polars as pl
import pytest

from opendata.tokyo_metropolitan_government.cultural_facilities_project import CSV_METADATA
from utils import csv_util


def test_metadata_has_required_keys():
    assert "target_url_list" in CSV_METADATA
    assert "header" in CSV_METADATA
    assert "dropna" in CSV_METADATA


def test_metadata_dropna_columns_are_in_header():
    for col in CSV_METADATA["dropna"]:
        assert col in CSV_METADATA["header"]


def test_replace_removes_comma_from_latitude():
    data = pl.DataFrame({"緯度": ["35,6762", "35.6762", "35,123,456"]})
    result = data.with_columns(csv_util.replace(data, "緯度", ",", "").alias("緯度"))
    assert result["緯度"].to_list() == ["356762", "35.6762", "35123456"]


def test_replace_does_not_affect_other_columns():
    data = pl.DataFrame({"緯度": ["35,6762"], "経度": ["139,6503"]})
    result = data.with_columns(csv_util.replace(data, "緯度", ",", "").alias("緯度"))
    assert result["経度"][0] == "139,6503"
