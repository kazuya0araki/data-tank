import os

_BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../data/csv/opendata/mhlw"))
OUTPUT_DESTINATION = _BASE + "/{}"
COVID_19_CSV = os.path.join(_BASE, "covid_19.csv")
DATASETS = [
    "covid_19",
]
