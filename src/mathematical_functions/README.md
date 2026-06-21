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
| `linear_function` | 一次関数 `y = x` | `Linear_Function.csv` |
| `quadratic_function` | 二次関数 `y = x²` | `Quadratic_Function.csv` |
| `cubic_function` | 三次関数 `y = x³` | `Cubic_Function.csv` |
| `square_root_function` | 平方根 `y = x^(1/2)` | `Square_Root_Function.csv` |
| `cubic_root_function` | 立方根 `y = x^(1/3)` | `Cubic_Root_Function.csv` |
| `two_to_the_xth_power_function` | 指数関数 `y = 2^x` | `Two_to_the_xth_Power_Function.csv` |
| `exponential_x_function` | 自然指数関数 `y = eˣ` | `Exponential_X_Function.csv` |
| `logarithm_function` | 自然対数 `y = ln(x)` | `Logarithm_Function.csv` |

### 三角関数

| dataset_name | 関数 | 出力ファイル |
|---|---|---|
| `sine` | sin `y = sin(x)` | `Sine.csv` |
| `cosine` | cos `y = cos(x)` | `Cosine.csv` |
| `tangent` | tan `y = tan(x)` | `Tangent.csv` |

### 媒介変数曲線

| dataset_name | 曲線 | 出力ファイル |
|---|---|---|
| `cycloid` | サイクロイド | `Cycloid.csv` |
| `astroid` | アストロイド | `Astroid.csv` |
| `cardioid` | カージオイド | `Cardioid.csv` |
| `circle` | 円 | `Circle.csv` |
| `logarithmic_spiral` | 対数螺旋 | `Logarithmic_Spiral.csv` |
| `lissajous_curve` | リサージュ曲線 | `Lissajous_Curve_1/2/3.csv` |
| `involute_curve` | インボリュート曲線 | `Involute_Curve.csv` |

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
