import polars as pl
import pytest

from opendata.tokyo_metropolitan_government.public_facilities import CSV_METADATA


def test_metadata_has_required_keys():
    assert "target_url_list" in CSV_METADATA
    assert "header" in CSV_METADATA
    assert "dropna" in CSV_METADATA


def test_metadata_dropna_columns_are_in_header():
    for col in CSV_METADATA["dropna"]:
        assert col in CSV_METADATA["header"]


def test_cast_parking_column_to_boolean():
    # Polars infers numeric 0/1 columns from CSV as Int64; cast Int64 → Boolean
    data = pl.DataFrame({"駐車場_有無": pl.Series([1, 0, 1], dtype=pl.Int64)})
    result = data.with_columns(pl.col("駐車場_有無").cast(pl.Boolean))
    assert result["駐車場_有無"].dtype == pl.Boolean
    assert result["駐車場_有無"].to_list() == [True, False, True]


def test_cast_fee_column_to_boolean():
    data = pl.DataFrame({"料金_要否": pl.Series([0, 1], dtype=pl.Int64)})
    result = data.with_columns(pl.col("料金_要否").cast(pl.Boolean))
    assert result["料金_要否"].dtype == pl.Boolean


def test_cast_both_boolean_columns_together():
    data = pl.DataFrame({
        "駐車場_有無": pl.Series([1, 0], dtype=pl.Int64),
        "料金_要否": pl.Series([0, 1], dtype=pl.Int64),
    })
    result = data.with_columns([
        pl.col("駐車場_有無").cast(pl.Boolean),
        pl.col("料金_要否").cast(pl.Boolean),
    ])
    assert result["駐車場_有無"].dtype == pl.Boolean
    assert result["料金_要否"].dtype == pl.Boolean
