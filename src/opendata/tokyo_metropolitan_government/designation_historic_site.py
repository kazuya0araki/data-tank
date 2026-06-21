import os

from utils import csv_util as util

# metadata
CSV_METADATA = {
  "target_url_list": [
    ["https://www.opendata.metro.tokyo.lg.jp/kyouiku/130001culturalproperty.csv", "cp932"],
  ],
  "header": ["都道府県名", "市区町村名", "名称", "文化財分類", "住所", "緯度", "経度", "所有者等", "文化財指定日", "備考"],
  "dropna": ["緯度", "経度"],
}

OUTPUT_DESTINATION = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../data/csv/opendata/tokyo_metropolitan_government/designation_historic_site/output.csv"))

# main
def main():
  # download and merge csv
  data = util.marge_csv(CSV_METADATA)

  # data preprocessing
  data = data.with_columns(util.strip(data, "名称").alias("名称"))
  data = util.distinct(data)

  # output data mart csv
  util.output_csv(data, OUTPUT_DESTINATION)

if __name__=="__main__":
  main()
