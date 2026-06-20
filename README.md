# Data Tank

画像・数学関数・オープンデータを CSV に変換・加工するデータ処理ツール集。

## 機能概要

| モジュール | 内容 | 詳細 |
|---|---|---|
| `image_sampling` | 画像の非白ピクセルを (x, y) 座標の CSV に変換 | [README](src/image_sampling/README.md) |
| `mathematical_functions` | 数学関数（初等関数・三角関数・媒介変数曲線）を CSV に出力 | [README](src/mathematical_functions/README.md) |
| `opendata/mhlw` | 厚生労働省オープンデータの取得・加工 | [README](src/opendata/README.md) |
| `opendata/tokyo_metropolitan_government` | 東京都オープンデータの取得・加工 | [README](src/opendata/README.md) |

## 動作環境

- Python 3.14.6+
- [uv](https://github.com/astral-sh/uv)

## セットアップ

```bash
git clone <repository-url>
cd data-tank
uv sync
```

## 使い方

### Image Sampling

画像ファイルを読み込み、二値化後に非白ピクセルの座標を CSV として `data/image_sampling/` に出力する。

```bash
uv run python -m image_sampling
```

`src/image_sampling/__main__.py` の `image_to_csv()` に対象画像のパスを指定する。

**入出力例**

```
images/Lenna.png  →  data/image_sampling/Lenna.csv
```

```csv
"x","y"
"0","10"
"1","10"
...
```

---

### Mathematical Functions

数学関数の (x, y) データを CSV として `data/csv/Mathematical Functions/` に出力する。

```bash
uv run python -m mathematical_functions --target <dataset_name>
```

**対応データセット**

| カテゴリ | 関数 |
|---|---|
| 初等関数 | 一次関数、二次関数、三次関数、平方根、立方根、指数関数 |
| 三角関数 | sin、cos、tan |
| 媒介変数曲線 | サイクロイド、アストロイド、カージオイド、円、対数螺旋、リサージュ曲線、インボリュート曲線 |

---

### Open Data — MHLW（厚生労働省）

厚生労働省のオープンデータを取得・結合して CSV を出力する。

```bash
uv run python -m opendata.mhlw --target <dataset_name>
```

| dataset_name | 内容 | 出力先 |
|---|---|---|
| `covid_19` | PCR 検査実施人数と陽性者数の結合データ | `data/opendata/mhlw/covid_19.csv` |

詳細は [src/opendata/README.md](src/opendata/README.md) を参照。

---

### Open Data — Tokyo Metropolitan Government（東京都）

東京都オープンデータを取得・加工して CSV を出力する。

```bash
uv run python -m opendata.tokyo_metropolitan_government --target <dataset_name>
```

| dataset_name | 内容 | 出力先 |
|---|---|---|
| `cultural_facilities_project` | 文化施設事業（イベント情報・緯度経度付き） | `data/Tokyo Metropolitan Government/Cultural Facilities Project/csv/output.csv` |
| `designation_historic_site` | 文化財指定地一覧 | `data/Tokyo Metropolitan Government/Designation Historic Site/csv/output.csv` |
| `life_and_statistics` | 生活と統計（区市町村別・年別の人口・世帯数等） | `data/Tokyo Metropolitan Government/Life and Statistics/csv/output.csv` |
| `public_facilities` | 公共施設一覧（駐車場・料金情報付き） | `data/Tokyo Metropolitan Government/Public Facilities/csv/output.csv` |

詳細は [src/opendata/README.md](src/opendata/README.md) を参照。

---

## ディレクトリ構成

```
data-tank/
├── src/
│   ├── image_sampling/
│   │   ├── main.py              # image_to_csv()
│   │   └── __main__.py
│   ├── mathematical_functions/
│   │   ├── create.py            # 各関数の CSV 生成
│   │   ├── const.py
│   │   └── __main__.py
│   ├── opendata/
│   │   ├── mhlw/
│   │   │   ├── covid_19.py
│   │   │   ├── const.py
│   │   │   └── __main__.py
│   │   └── tokyo_metropolitan_government/
│   │       ├── cultural_facilities_project.py
│   │       ├── designation_historic_site.py
│   │       ├── life_and_statistics.py
│   │       ├── public_facilities.py
│   │       ├── const.py
│   │       └── __main__.py
│   └── utils/
│       └── csv_util.py          # CSV 取得・加工の共通ユーティリティ
├── tests/                       # pytest テスト（コンポーネント別）
├── data/                        # 出力 CSV
├── images/                      # 入力画像
├── pyproject.toml
└── uv.lock
```

## テスト

```bash
uv run pytest tests/ -v
```

## 依存ライブラリ

| ライブラリ | 用途 |
|---|---|
| [polars](https://pola.rs/) | CSV 取得・加工 |
| [numpy](https://numpy.org/) | 数学関数の計算 |
| [matplotlib](https://matplotlib.org/) | グラフ描画（予定） |
| [opencv-python](https://github.com/opencv/opencv-python) | 画像の読み込み・二値化 |
