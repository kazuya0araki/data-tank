

import argparse

from . import const

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Mathematical Functions",
        usage="python -m mathematical_functions --target {dataset_name}",
        description="数学関数データ",
        epilog="end",
        add_help=True,
    )

    parser.add_argument("-T", "--target", type=str, dest="target", required=True, help="対象データセット名({})".format(const.DATASETS))

    args = parser.parse_args()

    # match args.target:
    #     case "covid_19":
    #         covid_19.main()
    #     case _:
    #         print(args.target, "is not found. Please select: {}".format(const.DATASETS))