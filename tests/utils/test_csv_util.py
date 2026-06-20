import polars as pl
import pytest

from utils.csv_util import (
    distinct,
    download_csv,
    join_csv,
    marge_csv,
    output_csv,
    replace,
    strip,
)


# --- download_csv ---

def test_download_csv_selects_columns(tmp_path):
    f = tmp_path / "t.csv"
    f.write_text("a,b,c\n1,2,3\n", encoding="utf-8")
    result = download_csv(str(f), "utf8", ["a", "c"], ["a"])
    assert result.columns == ["a", "c"]


def test_download_csv_drops_nulls(tmp_path):
    f = tmp_path / "t.csv"
    f.write_text("a,b\n1,2\n3,\n5,6\n", encoding="utf-8")
    result = download_csv(str(f), "utf8", ["a", "b"], ["b"])
    assert result.shape == (2, 2)
    assert result["a"].to_list() == [1, 5]


def test_download_csv_non_utf8_encoding(tmp_path):
    f = tmp_path / "t.csv"
    f.write_bytes("名前,値\n東京,100\n大阪,\n".encode("cp932"))
    result = download_csv(str(f), "cp932", ["名前", "値"], ["値"])
    assert result.shape == (1, 2)
    assert result["名前"][0] == "東京"


# --- marge_csv ---

def test_marge_csv_concatenates_all_files(tmp_path):
    f1 = tmp_path / "f1.csv"
    f2 = tmp_path / "f2.csv"
    f1.write_text("name,val\nalice,1\n", encoding="utf-8")
    f2.write_text("name,val\nbob,2\n", encoding="utf-8")
    metadata = {
        "target_url_list": [[str(f1), "utf8"], [str(f2), "utf8"]],
        "header": ["name", "val"],
        "dropna": ["name"],
    }
    result = marge_csv(metadata)
    assert result.shape == (2, 2)
    assert set(result["name"].to_list()) == {"alice", "bob"}


def test_marge_csv_processes_all_files_not_just_first(tmp_path):
    files = []
    for i in range(3):
        f = tmp_path / f"f{i}.csv"
        f.write_text(f"x\n{i}\n", encoding="utf-8")
        files.append([str(f), "utf8"])
    metadata = {"target_url_list": files, "header": ["x"], "dropna": ["x"]}
    result = marge_csv(metadata)
    assert result.shape == (3, 1)


# --- join_csv ---

def test_join_csv_left_keeps_all_left_rows():
    left = pl.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
    right = pl.DataFrame({"id": [1, 2], "other": ["x", "y"]})
    result = join_csv(left, "left", right, "id")
    assert result.shape[0] == 3


def test_join_csv_inner_keeps_only_matches():
    left = pl.DataFrame({"id": [1, 2, 3]})
    right = pl.DataFrame({"id": [1, 2]})
    result = join_csv(left, "inner", right, "id")
    assert result.shape[0] == 2


def test_join_csv_outer_maps_to_full():
    left = pl.DataFrame({"id": [1, 2]})
    right = pl.DataFrame({"id": [2, 3]})
    result = join_csv(left, "outer", right, "id")
    assert result.shape[0] == 3


def test_join_csv_unknown_type_falls_back_to_left():
    left = pl.DataFrame({"id": [1, 2, 3]})
    right = pl.DataFrame({"id": [1, 2]})
    result = join_csv(left, "unknown", right, "id")
    assert result.shape[0] == 3


# --- replace ---

def test_replace_removes_commas():
    df = pl.DataFrame({"val": ["1,000", "2,500", "3"]})
    result = replace(df, "val", ",", "")
    assert result.to_list() == ["1000", "2500", "3"]


def test_replace_all_occurrences():
    df = pl.DataFrame({"val": ["a,b,c"]})
    result = replace(df, "val", ",", "-")
    assert result[0] == "a-b-c"


# --- strip ---

def test_strip_removes_whitespace():
    df = pl.DataFrame({"name": ["  hello  ", "world ", " foo"]})
    result = strip(df, "name")
    assert result.to_list() == ["hello", "world", "foo"]


def test_strip_no_op_on_clean_strings():
    df = pl.DataFrame({"name": ["clean"]})
    result = strip(df, "name")
    assert result[0] == "clean"


# --- distinct ---

def test_distinct_removes_duplicates():
    df = pl.DataFrame({"a": [1, 2, 2, 3], "b": ["x", "y", "y", "z"]})
    result = distinct(df)
    assert result.shape == (3, 2)


def test_distinct_no_op_when_already_unique():
    df = pl.DataFrame({"a": [1, 2, 3]})
    result = distinct(df)
    assert result.shape == (3, 1)


# --- output_csv ---

def test_output_csv_creates_file(tmp_path):
    out = tmp_path / "output.csv"
    df = pl.DataFrame({"name": ["alice", "bob"], "val": [1, 2]})
    output_csv(df, str(out))
    assert out.exists()


def test_output_csv_content_is_quoted(tmp_path):
    out = tmp_path / "output.csv"
    df = pl.DataFrame({"name": ["alice"], "val": [1]})
    output_csv(df, str(out))
    content = out.read_text(encoding="utf-8")
    assert '"alice"' in content
    assert '"name"' in content


def test_output_csv_roundtrip(tmp_path):
    out = tmp_path / "output.csv"
    df = pl.DataFrame({"a": ["x", "y"], "b": [1, 2]})
    output_csv(df, str(out))
    loaded = pl.read_csv(str(out))
    assert loaded["a"].to_list() == ["x", "y"]
