import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Print the states with the most IPC crimes for a year."
    )
    parser.add_argument("--year", required=True, help="year to report")
    parser.add_argument("--top", type=int, default=5, help="number of states to report")
    args = parser.parse_args()

    data_dir = Path(__file__).parent / "crime"
    available_years = set()
    totals = {}

    for path in sorted(data_dir.glob("01_District_wise_crimes_committed_IPC_*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            columns = {name.strip().upper(): name for name in reader.fieldnames}
            state_column = columns.get("STATE/UT", columns.get("STATES/UTS"))
            district_column = columns.get("DISTRICT")
            year_column = columns.get("YEAR")
            crimes_column = columns.get("TOTAL IPC CRIMES")

            for row in reader:
                year = row[year_column].strip()
                available_years.add(year)
                if year != args.year or "TOTAL" in row[district_column].upper():
                    continue

                state = row[state_column].strip()
                crimes = int(row[crimes_column])
                totals[state] = totals.get(state, 0) + crimes

    if args.year not in available_years:
        parser.error(
            "year {} is unavailable; available years: {}".format(
                args.year, ", ".join(sorted(available_years))
            )
        )

    all_india_total = sum(totals.values())
    for state, total in sorted(totals.items(), key=lambda item: (-item[1], item[0]))[
        : args.top
    ]:
        percentage = total / all_india_total * 100
        print("{}: {:,} ({:.1f}%)".format(state, total, percentage))


if __name__ == "__main__":
    main()
