import numpy as np
import pytest

from mathematical_functions import const, create


@pytest.fixture(autouse=True)
def patch_data_path(tmp_path, monkeypatch):
    monkeypatch.setattr(const, "DATA_PATH", str(tmp_path) + "/")


# --- elementary functions ---

def test_create_linear_function_csv(tmp_path):
    create.create_linear_function_csv()
    data = np.loadtxt(tmp_path / "Linear_Function.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 0], data[:, 1])


def test_create_quadratic_function_csv(tmp_path):
    create.create_quadratic_function_csv()
    data = np.loadtxt(tmp_path / "Quadratic_Function.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 1], data[:, 0] ** 2, rtol=1e-9)


def test_create_cubic_function_csv(tmp_path):
    create.create_cubic_function_csv()
    data = np.loadtxt(tmp_path / "Cubic_Function.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 1], data[:, 0] ** 3, rtol=1e-9)


def test_create_square_root_function_csv(tmp_path):
    create.create_square_root_function_csv()
    data = np.loadtxt(tmp_path / "Square_Root_Function.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 1], data[:, 0] ** 0.5, rtol=1e-9)


def test_create_cubic_root_function_csv(tmp_path):
    create.create_cubic_root_function_csv()
    data = np.loadtxt(tmp_path / "Cubic_Root_Function.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 1], data[:, 0] ** (1 / 3), rtol=1e-9)


def test_create_exponential_x_function_csv(tmp_path):
    create.create_exponential_x_function_csv()
    data = np.loadtxt(tmp_path / "Exponential_X_Function.csv", delimiter=",", skiprows=1)
    # rtol=1e-6: values are serialized with fmt="%.10f", so precision is limited
    np.testing.assert_allclose(data[:, 1], np.exp(data[:, 0]), rtol=1e-6)


# --- trigonometric functions ---

def test_create_sine_function_csv(tmp_path):
    create.create_sine_function_csv()
    data = np.loadtxt(tmp_path / "Sine.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 1], np.sin(data[:, 0]), atol=1e-9)


def test_create_cosine_function_csv(tmp_path):
    create.create_cosine_function_csv()
    data = np.loadtxt(tmp_path / "Cosine.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 1], np.cos(data[:, 0]), atol=1e-9)


def test_create_tangent_function_csv(tmp_path):
    create.create_tangent_function_csv()
    data = np.loadtxt(tmp_path / "Tangent.csv", delimiter=",", skiprows=1)
    # Skip near-discontinuity points where tan diverges (|tan| > 1e6)
    finite = np.abs(data[:, 1]) < 1e6
    np.testing.assert_allclose(data[finite, 1], np.tan(data[finite, 0]), atol=1e-6)


# --- parametric curves ---

def test_create_cycloid_csv(tmp_path):
    create.create_cycloid_csv()
    data = np.loadtxt(tmp_path / "Cycloid.csv", delimiter=",", skiprows=1)
    r = np.linspace(0, 2 * np.pi, 361)
    np.testing.assert_allclose(data[:, 0], r - np.sin(r), atol=1e-9)
    np.testing.assert_allclose(data[:, 1], 1 - np.cos(r), atol=1e-9)


def test_create_circle_csv(tmp_path):
    create.create_circle_csv()
    data = np.loadtxt(tmp_path / "Circle.csv", delimiter=",", skiprows=1)
    # All points should lie on the unit circle
    np.testing.assert_allclose(data[:, 0] ** 2 + data[:, 1] ** 2, 1.0, atol=1e-9)


def test_create_astroid_csv(tmp_path):
    create.create_astroid_csv()
    data = np.loadtxt(tmp_path / "Astroid.csv", delimiter=",", skiprows=1)
    # Astroid identity: |x|^(2/3) + |y|^(2/3) = 1
    np.testing.assert_allclose(
        np.abs(data[:, 0]) ** (2 / 3) + np.abs(data[:, 1]) ** (2 / 3),
        1.0,
        atol=1e-9,
    )


def test_create_two_to_the_xth_power_function_csv(tmp_path):
    create.create_two_to_the_xth_power_function_csv()
    data = np.loadtxt(tmp_path / "Two_to_the_xth_Power_Function.csv", delimiter=",", skiprows=1)
    np.testing.assert_allclose(data[:, 1], 2 ** data[:, 0], rtol=1e-6)


def test_create_logarithm_function_csv(tmp_path):
    create.create_logarithm_function_csv()
    data = np.loadtxt(tmp_path / "Logarithm_Function.csv", delimiter=",", skiprows=1)
    assert (data[:, 0] > 0).all()
    np.testing.assert_allclose(data[:, 1], np.log(data[:, 0]), rtol=1e-9)


def test_create_cardioid_csv(tmp_path):
    create.create_cardioid_csv()
    data = np.loadtxt(tmp_path / "Cardioid.csv", delimiter=",", skiprows=1)
    assert data.shape == (361, 2)


def test_create_logarithmic_spiral_csv(tmp_path):
    create.create_general_csv()
    data = np.loadtxt(tmp_path / "Logarithmic_Spiral.csv", delimiter=",", skiprows=1)
    r4 = np.linspace(0, 4 * np.pi, 721)
    np.testing.assert_allclose(data[:, 0], np.exp(r4 / 4) * np.cos(r4), rtol=1e-6, atol=1e-9)
    np.testing.assert_allclose(data[:, 1], np.exp(r4 / 4) * np.sin(r4), rtol=1e-6, atol=1e-9)


def test_create_lissajous_curve_csv(tmp_path):
    create.create_lissajous_curve_csv()
    assert (tmp_path / "Lissajous_Curve_1.csv").exists()
    assert (tmp_path / "Lissajous_Curve_2.csv").exists()
    assert (tmp_path / "Lissajous_Curve_3.csv").exists()
    data = np.loadtxt(tmp_path / "Lissajous_Curve_1.csv", delimiter=",", skiprows=1)
    assert data.shape == (721, 2)


def test_create_involute_curve_csv(tmp_path):
    create.create_involute_curve_csv()
    data = np.loadtxt(tmp_path / "Involute_Curve.csv", delimiter=",", skiprows=1)
    r4 = np.linspace(0, 4 * np.pi, 721)
    np.testing.assert_allclose(data[:, 0], np.cos(r4) + r4 * np.sin(r4), atol=1e-9)
    np.testing.assert_allclose(data[:, 1], np.sin(r4) - r4 * np.cos(r4), atol=1e-9)
