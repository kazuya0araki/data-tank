# Mathematical Functions

数学関数の (x, y) データを CSV として出力する。

## 実行

```bash
uv run python -m mathematical_functions --target <dataset_name>
```

## 対応データセット

### 初等関数

| dataset_name | 関数 | 出力ファイル |
|---|---|---|
| *(未実装)* | 一次関数 `y = x` | `Linear_Function.csv` |
| *(未実装)* | 二次関数 `y = x²` | `Quadratic_Function.csv` |
| *(未実装)* | 三次関数 `y = x³` | `Cubic_Function.csv` |
| *(未実装)* | 平方根 `y = x^(1/2)` | `Square_Root_Function.csv` |
| *(未実装)* | 立方根 `y = x^(1/3)` | `Cubic_Root_Function.csv` |
| *(未実装)* | 指数関数 `y = eˣ` | `Exponential_X_Function.csv` |

### 三角関数

| dataset_name | 関数 | 出力ファイル |
|---|---|---|
| *(未実装)* | sin `y = sin(x)` | `Sine.csv` |
| *(未実装)* | cos `y = cos(x)` | `Cosine.csv` |
| *(未実装)* | tan `y = tan(x)` | `Tangent.csv` |

### 媒介変数曲線

| dataset_name | 曲線 | 出力ファイル |
|---|---|---|
| *(未実装)* | サイクロイド | `Cycloid.csv` |
| *(未実装)* | アストロイド | `Astroid.csv` |
| *(未実装)* | カージオイド | `Cardioid.csv` |
| *(未実装)* | 円 | `Circle.csv` |
| *(未実装)* | 対数螺旋 | `Logarithmic_Spiral.csv` |
| *(未実装)* | リサージュ曲線 | `Lissajous_Curve_1/2/3.csv` |
| *(未実装)* | インボリュート曲線 | `Involute_Curve.csv` |

## 出力先

```
data/csv/Mathematical Functions/<filename>.csv
```

**出力フォーマット**

```csv
x,y
-10.0000000000,-10.0000000000
-9.9000000000,-9.9000000000
...
```
