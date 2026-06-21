from typing import Annotated

import typer

from . import const, covid_19

app = typer.Typer(help="厚生労働省のデータ")


@app.command()
def main(
    target: Annotated[str, typer.Option("--target", "-T", help=f"対象データセット名 {const.DATASETS}")],
):
    match target:
        case "covid_19":
            covid_19.main()
        case _:
            typer.echo(f"{target} is not found. Please select: {const.DATASETS}", err=True)
            raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
