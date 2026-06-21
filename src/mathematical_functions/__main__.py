import os
from typing import Annotated

import typer

from . import const, create

app = typer.Typer(help="数学関数データ")


@app.command()
def main(
    target: Annotated[str, typer.Option("--target", "-T", help=f"対象データセット名 {const.MATH_DATASETS}")],
):
    os.makedirs(const.DATA_PATH, exist_ok=True)
    match target:
        case "linear_function":
            create.create_linear_function_csv()
        case "quadratic_function":
            create.create_quadratic_function_csv()
        case "cubic_function":
            create.create_cubic_function_csv()
        case "square_root_function":
            create.create_square_root_function_csv()
        case "cubic_root_function":
            create.create_cubic_root_function_csv()
        case "two_to_the_xth_power_function":
            create.create_two_to_the_xth_power_function_csv()
        case "exponential_x_function":
            create.create_exponential_x_function_csv()
        case "logarithm_function":
            create.create_logarithm_function_csv()
        case "sine":
            create.create_sine_function_csv()
        case "cosine":
            create.create_cosine_function_csv()
        case "tangent":
            create.create_tangent_function_csv()
        case "cycloid":
            create.create_cycloid_csv()
        case "astroid":
            create.create_astroid_csv()
        case "cardioid":
            create.create_cardioid_csv()
        case "circle":
            create.create_circle_csv()
        case "logarithmic_spiral":
            create.create_general_csv()
        case "lissajous_curve":
            create.create_lissajous_curve_csv()
        case "involute_curve":
            create.create_involute_curve_csv()
        case _:
            typer.echo(f"{target} is not found. Please select: {const.MATH_DATASETS}", err=True)
            raise typer.Exit(code=1)
    print("* CSV出力が完了しました")


if __name__ == "__main__":
    app()
