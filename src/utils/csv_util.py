# Standard Library
import io
import os
import urllib.request

# Third Party Library
import polars as pl


def download_csv(target_csv, csv_charset, csv_header, csv_dropna):
    if csv_charset in ("utf8", "utf8-lossy"):
        df = pl.read_csv(target_csv, encoding=csv_charset)
    elif str(target_csv).startswith(("http://", "https://")):
        with urllib.request.urlopen(target_csv) as resp:  # noqa: S310
            df = pl.read_csv(io.StringIO(resp.read().decode(csv_charset)))
    else:
        with open(target_csv, "rb") as f:
            df = pl.read_csv(io.StringIO(f.read().decode(csv_charset)))
    return df.select(csv_header).drop_nulls(subset=csv_dropna)


def marge_csv(csv_metadata):
    frames = [
        download_csv(target_csv[0], target_csv[1], csv_metadata["header"], csv_metadata["dropna"])
        for target_csv in csv_metadata["target_url_list"]
    ]
    if len(frames) <= 1:
        return frames[0] if frames else pl.DataFrame()
    first_schema = frames[0].schema
    cols_to_str = [
        col for col in first_schema
        if any(f.schema.get(col) != first_schema[col] for f in frames[1:])
    ]
    if cols_to_str:
        frames = [f.with_columns([pl.col(c).cast(pl.String) for c in cols_to_str]) for f in frames]
    return pl.concat(frames)


def join_csv(left_data, join_type, right_data, on_key):
    _map = {"outer": "full"}
    how = _map.get(join_type, join_type)
    if how in ("left", "right", "inner", "full", "cross"):
        return left_data.join(right_data, on=on_key, how=how)
    return left_data.join(right_data, on=on_key, how="left")


def replace(data, column, trim_strings, replace_strings):
    return data[column].str.replace_all(trim_strings, replace_strings)


def strip(data, column):
    return data[column].str.strip_chars()


def distinct(data):
    return data.unique()


def output_csv(data, output_destination):
    dest_dir = os.path.dirname(output_destination)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    data.write_csv(output_destination, quote_style="always")
    print("* CSV出力が完了しました")
