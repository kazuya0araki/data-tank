from utils import csv_util as util
import polars as pl

# metadata
CSV_METADATA = {
  "target_url_list": [
    ["https://www.toukei.metro.tokyo.lg.jp/kurasi/2019/csv/ku19rv2310.csv", "utf8"],
    ["https://www.toukei.metro.tokyo.lg.jp/kurasi/2020/csv/ku20rv2310.csv", "utf8"],
    ["https://www.toukei.metro.tokyo.lg.jp/kurasi/2021/csv/ku21rv2310.csv", "utf8"],
    ["https://www.toukei.metro.tokyo.lg.jp/kurasi/2022/csv/ku22rv2310.csv", "utf8"],
    ["https://www.toukei.metro.tokyo.lg.jp/kurasi/2023/csv/ku23rv2310.csv", "utf8"],
  ],
  "header": ["地域階層", "地域", "面積（平方キロメートル）", "人口／総数（人）", "人口／男（人）", "人口／女（人）", "65歳以上人口の割合（％）", "（参考）世帯数（世帯）", "小学校児童数（人）", "中学校生徒数（人）"],
  "dropna": ["地域"],
  "year": [2019, 2020, 2021, 2022, 2023],
}

OUTPUT_DESTINATION = "../../../data/Tokyo Metropolitan Government/Life and Statistics/csv/output.csv"

# main
def main():
  # download csv
  frames = []
  for index, target_csv in enumerate(CSV_METADATA["target_url_list"]):
    subdata = util.download_csv(target_csv[0], target_csv[1], CSV_METADATA["header"], CSV_METADATA["dropna"])
    subdata = subdata.with_columns(pl.lit(CSV_METADATA["year"][index]).alias("年")).select(["年", *CSV_METADATA["header"]])
    frames.append(subdata)
  data = pl.concat(frames)

  # data preprocessing
  data = (
    data.filter(pl.col("地域階層") == "2")
    .drop("地域階層")
    .with_columns(
      (pl.col("65歳以上人口の割合（％）").cast(pl.Float64) / 100).alias("65歳以上人口の割合（％）")
    )
    .cast({
      "年": pl.Int64,
      "人口／総数（人）": pl.Int64,
      "人口／男（人）": pl.Int64,
      "人口／女（人）": pl.Int64,
      "（参考）世帯数（世帯）": pl.Int64,
      "小学校児童数（人）": pl.Int64,
      "中学校生徒数（人）": pl.Int64,
    })
    .rename({
      "地域": "市区町村",
      "面積（平方キロメートル）": "面積(㎢)",
      "人口／総数（人）": "人口(総数)",
      "人口／男（人）": "人口(男性)",
      "人口／女（人）": "人口(女性)",
      "65歳以上人口の割合（％）": "65歳以上人口の割合",
      "（参考）世帯数（世帯）": "世帯数",
      "小学校児童数（人）": "小学校児童数",
      "中学校生徒数（人）": "中学校生徒数",
    })
  )

  # output data mart csv
  util.output_csv(data, OUTPUT_DESTINATION)

if __name__=="__main__":
  main()
