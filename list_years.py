import csv
from pathlib import Path

import pandas as pd


crime_dir = Path(__file__).parent / "crime"
years = set()

for csv_path in crime_dir.glob("*.csv"):
    try:
        data = pd.read_csv(csv_path)
    except pd.errors.ParserError:
        # Some source files contain rows with unescaped commas. Read those
        # files permissively so a malformed row doesn't hide their years.
        with csv_path.open(newline="", encoding="utf-8-sig") as csv_file:
            rows = csv.reader(csv_file)
            header = next(rows, [])
            year_index = next(
                (
                    index
                    for index, column in enumerate(header)
                    if column.casefold() == "year"
                ),
                None,
            )
            if year_index is not None:
                for row in rows:
                    if len(row) > year_index:
                        year = row[year_index]
                        if year.strip() and year.casefold() not in {
                            "#n/a",
                            "#n/a n/a",
                            "#na",
                            "-1.#ind",
                            "-1.#qnan",
                            "-nan",
                            "1.#ind",
                            "1.#qnan",
                            "<na>",
                            "n/a",
                            "na",
                            "nan",
                            "none",
                            "null",
                        }:
                            years.add(year)
        continue
    year_column = next(
        (column for column in data.columns if column.casefold() == "year"), None
    )
    if year_column is not None:
        years.update(data[year_column].dropna().astype(str))

for year in sorted(years):
    print(year)
