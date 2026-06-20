import polars as pl
import pytest

from opendata.tokyo_metropolitan_government.life_and_statistics import CSV_METADATA


def test_metadata_has_required_keys():
    assert "target_url_list" in CSV_METADATA
    assert "header" in CSV_METADATA
    assert "dropna" in CSV_METADATA
    assert "year" in CSV_METADATA


def test_metadata_year_count_matches_url_count():
    assert len(CSV_METADATA["year"]) == len(CSV_METADATA["target_url_list"])


def test_filter_by_region_level():
    data = pl.DataFrame({
        "地域階層": ["1", "2", "2", "3"],
        "地域": ["東京都", "千代田区", "中央区", "丸の内"],
    })
    result = data.filter(pl.col("地域階層") == "2")
    assert result.shape[0] == 2
    assert set(result["地域"].to_list()) == {"千代田区", "中央区"}


def test_drop_region_level_column():
    data = pl.DataFrame({"地域階層": ["2"], "地域": ["千代田区"], "年": [2019]})
    result = data.filter(pl.col("地域階層") == "2").drop("地域階層")
    assert "地域階層" not in result.columns


def test_percentage_column_divided_by_100():
    data = pl.DataFrame({"65歳以上人口の割合（％）": ["25.5", "18.0"]})
    result = data.with_columns(
        (pl.col("65歳以上人口の割合（％）").cast(pl.Float64) / 100).alias("65歳以上人口の割合（％）")
    )
    assert result["65歳以上人口の割合（％）"].to_list() == pytest.approx([0.255, 0.18])


def test_integer_columns_cast_correctly():
    data = pl.DataFrame({
        "年": ["2019"],
        "人口／総数（人）": ["1000"],
    })
    result = data.cast({"年": pl.Int64, "人口／総数（人）": pl.Int64})
    assert result["年"].dtype == pl.Int64
    assert result["人口／総数（人）"].dtype == pl.Int64


def test_year_column_prepended_first():
    import polars as pl
    base_cols = ["地域階層", "地域"]
    subdata = pl.DataFrame({"地域階層": ["2"], "地域": ["千代田区"]})
    subdata = subdata.with_columns(pl.lit(2019).alias("年")).select(["年", *subdata.columns])
    assert subdata.columns[0] == "年"
    assert subdata["年"][0] == 2019


def test_rename_columns():
    data = pl.DataFrame({
        "地域": ["千代田区"],
        "面積（平方キロメートル）": ["11.66"],
    })
    result = data.rename({"地域": "市区町村", "面積（平方キロメートル）": "面積(㎢)"})
    assert "市区町村" in result.columns
    assert "面積(㎢)" in result.columns
    assert "地域" not in result.columns
