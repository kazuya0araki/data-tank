# Standard Library
import csv
from logging import exception

# Third Party Library
import polars as pl

# First Party Library
from utils import csv_util

# Local Library
from . import const

# const
PCR_CSV_METADATA = {
    "target_url_list": [["https://www.mhlw.go.jp/content/001060467.csv", "utf8"]],
    "header": ["日付", "PCR 検査実施人数(単日)"],
    "dropna": ["日付"],
}
PCR_RENAMED_HEADER = {"日付": "date", "PCR 検査実施人数(単日)": "tests"}
POSITIVE_CSV_METADATA = {
    "target_url_list": [["https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv", "utf8"]],
    "header": ["Date", "ALL"],
    "dropna": ["Date"],
}
POSITIVE_RENAMED_HEADER = {"Date": "date", "ALL": "positives"}


# main
def main():
    # download csv and merge data
    pcr_data = csv_util.marge_csv(PCR_CSV_METADATA)
    positive_data = csv_util.marge_csv(POSITIVE_CSV_METADATA)

    # data preprocessing
    pcr_data = pcr_data.rename(PCR_RENAMED_HEADER).fill_null(0).with_columns(pl.col("tests").cast(pl.Int64))
    positive_data = positive_data.rename(POSITIVE_RENAMED_HEADER).with_columns(pl.col("positives").cast(pl.Int64))
    data = csv_util.join_csv(pcr_data, "left", positive_data, "date")

    # output csv
    try:
        csv_util.output_csv(data, const.COVID_19_CSV)
    except csv.Error as e:
        exception(e)
