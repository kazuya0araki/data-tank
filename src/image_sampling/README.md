# Image Sampling

画像ファイルを読み込み、二値化後の非白ピクセルを (x, y) 座標の CSV として出力する。

## 処理フロー

1. 画像を読み込み BGR → RGB に変換
2. 閾値 127 で二値化（THRESH_BINARY）
3. 白 (255, 255, 255) 以外のピクセルを抽出して座標を記録
4. `data/image_sampling/<ファイル名>.csv` に出力

## 実行

```bash
uv run python -m image_sampling
```

`src/image_sampling/__main__.py` の `image_to_csv()` に対象画像のパスを指定する。

## 入出力

| | パス |
|---|---|
| 入力画像 | `images/<filename>.{png,jpg}` |
| 出力 CSV | `data/image_sampling/<filename>.csv` |

**出力フォーマット**

```csv
"x","y"
"0","10"
"1","10"
```

## サンプル画像

| ファイル | 説明 |
|---|---|
| `images/Lenna.png` | 標準テスト画像（Lenna） |
| `images/YOASOBI.jpg` | サンプル画像 |
