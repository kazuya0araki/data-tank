
import os


MATH_DATASETS = [
    # elementary functions
    "linear_function",
    "quadratic_function",
    "cubic_function",
    "square_root_function",
    "cubic_root_function",
    "two_to_the_xth_power_function",
    "exponential_x_function",
    "logarithm_function",
    # trigonometric functions
    "sine",
    "cosine",
    "tangent",
    # parametric curves
    "cycloid",
    "astroid",
    "cardioid",
    "circle",
    "logarithmic_spiral",
    "lissajous_curve",
    "involute_curve",
]
DATA_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data/csv/mathematical_functions")) + "/"
