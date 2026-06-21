from typing import Annotated

import typer

from . import const, cultural_facilities_project, designation_historic_site, life_and_statistics, public_facilities

app = typer.Typer(help="東京都オープンデータ")


@app.command()
def main(
    target: Annotated[str, typer.Option("--target", "-T", help=f"対象データセット名 {const.DATASETS}")],
):
    match target:
        case "cultural_facilities_project":
            cultural_facilities_project.main()
        case "designation_historic_site":
            designation_historic_site.main()
        case "life_and_statistics":
            life_and_statistics.main()
        case "public_facilities":
            public_facilities.main()
        case _:
            typer.echo(f"{target} is not found. Please select: {const.DATASETS}", err=True)
            raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
