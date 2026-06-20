import csv

import cv2 as cv
import numpy as np
import pytest

from image_sampling.main import image_to_csv


def _write_image(path, pixel_array):
    cv.imwrite(str(path), pixel_array)


@pytest.fixture()
def output_dir(tmp_path, monkeypatch):
    data_dir = tmp_path / "data" / "image_sampling"
    data_dir.mkdir(parents=True)
    monkeypatch.chdir(tmp_path)
    return data_dir


def test_image_to_csv_creates_output_file(tmp_path, output_dir):
    img = np.zeros((3, 3, 3), dtype=np.uint8)
    img_path = tmp_path / "sample.png"
    _write_image(img_path, img)

    image_to_csv(str(img_path))

    assert (output_dir / "sample.csv").exists()


def test_image_to_csv_output_has_xy_columns(tmp_path, output_dir):
    img = np.zeros((3, 3, 3), dtype=np.uint8)
    img_path = tmp_path / "sample.png"
    _write_image(img_path, img)

    image_to_csv(str(img_path))

    with open(output_dir / "sample.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert all("x" in row and "y" in row for row in rows)


def test_image_to_csv_white_pixels_excluded(tmp_path, output_dir):
    # All-white image: no pixels should be sampled
    img = np.full((4, 4, 3), 255, dtype=np.uint8)
    img_path = tmp_path / "white.png"
    _write_image(img_path, img)

    image_to_csv(str(img_path))

    with open(output_dir / "white.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert rows == []


def test_image_to_csv_black_pixels_included(tmp_path, output_dir):
    # All-black image: all pixels should be sampled
    img = np.zeros((2, 3, 3), dtype=np.uint8)
    img_path = tmp_path / "black.png"
    _write_image(img_path, img)

    image_to_csv(str(img_path))

    with open(output_dir / "black.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 6  # 2 rows × 3 cols


def test_image_to_csv_pixel_coordinates_correct(tmp_path, output_dir):
    # Single pixel image
    img = np.zeros((1, 1, 3), dtype=np.uint8)
    img_path = tmp_path / "dot.png"
    _write_image(img_path, img)

    image_to_csv(str(img_path))

    with open(output_dir / "dot.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 1
    assert rows[0]["x"] == "0"
    assert rows[0]["y"] == "0"
