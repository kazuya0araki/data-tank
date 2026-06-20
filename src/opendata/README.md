# Open Data

公的機関のオープンデータを取得・加工して CSV を出力する。

## MHLW（厚生労働省）

```bash
uv run python -m opendata.mhlw --target <dataset_name>
```

| dataset_name | 説明 | 出力先 |
|---|---|---|
| `covid_19` | PCR 検査実施人数と新規陽性者数の結合データ | `data/opendata/mhlw/covid_19.csv` |

**データソース**

| データ | URL |
|---|---|
| PCR 検査実施人数 | https://www.mhlw.go.jp/content/001060467.csv |
| 新規陽性者数（日別） | https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv |
| オープンデータ一覧 | https://www.mhlw.go.jp/stf/covid-19/open-data.html |

---

## Tokyo Metropolitan Government（東京都）

```bash
uv run python -m opendata.tokyo_metropolitan_government --target <dataset_name>
```

| dataset_name | 説明 | 出力先 |
|---|---|---|
| `cultural_facilities_project` | 都立文化施設事業一覧（イベント・緯度経度付き） | `data/Tokyo Metropolitan Government/Cultural Facilities Project/csv/output.csv` |
| `designation_historic_site` | 東京都指定史跡データ一覧 | `data/Tokyo Metropolitan Government/Designation Historic Site/csv/output.csv` |
| `life_and_statistics` | くらしと統計 区市町村統計表（2019〜2023年） | `data/Tokyo Metropolitan Government/Life and Statistics/csv/output.csv` |
| `public_facilities` | 公共施設一覧（駐車場・料金情報付き） | `data/Tokyo Metropolitan Government/Public Facilities/csv/output.csv` |

**データソース**

| dataset_name | データカタログ |
|---|---|
| `cultural_facilities_project` | [令和4年度](https://catalog.data.metro.tokyo.lg.jp/dataset/t313360d0000000001/resource/8170c629-279f-45ec-9c61-2650a63fcb5b) / [令和5年度](https://catalog.data.metro.tokyo.lg.jp/dataset/t313360d0000000001/resource/996a42ee-2929-4461-a77a-92e6873f3805) |
| `designation_historic_site` | [東京都指定史跡データ一覧](https://catalog.data.metro.tokyo.lg.jp/dataset/t000021d0000000025/resource/6fb22ee3-5138-4fee-b611-e041f2e47351) |
| `life_and_statistics` | [2019](https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000034/resource/93974346-92a7-47cb-a502-3603d68d3948) / [2020](https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000062/resource/f4f29555-63f2-42a9-b4ea-a9e47e0849d6) / [2021](https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000148/resource/82ec111b-83a6-41da-9201-0c7bd92686a0) / [2022](https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000151/resource/a6e40201-5baa-4d6e-8875-640f74ea4cd7) / [2023](https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000578/resource/addb83e6-ba1a-4569-9ce2-ff1f5269ad4c) |
| `public_facilities` | [公共施設一覧](https://catalog.data.metro.tokyo.lg.jp/dataset/t000003d0000000033/resource/27d1ce20-9023-4690-944c-5da47ed1427e) |
