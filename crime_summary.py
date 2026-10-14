import os
import pandas as pd


def load_data():
    csv_path = os.path.join(
        os.path.dirname(__file__),
        "crime",
        "01_District_wise_crimes_committed_IPC_2001_2012.csv",
    )
    return pd.read_csv(csv_path)


def top_states(df):
    totals = df[df["DISTRICT"] == "TOTAL"]
    grouped = totals.groupby("STATE/UT")["TOTAL IPC CRIMES"].sum()
    return grouped.nlargest(10)


def yearly_totals(df):
    totals = df[df["DISTRICT"] == "TOTAL"]
    return totals.groupby("YEAR")["TOTAL IPC CRIMES"].sum()


if __name__ == "__main__":
    df = load_data()
    print("Top 10 States/UTs by Total IPC Crimes:")
    print(top_states(df))
    print("\nYearly Totals of Total IPC Crimes:")
    print(yearly_totals(df))
