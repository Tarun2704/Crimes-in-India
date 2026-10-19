import os
import pandas as pd


def load_data(filepath=None):
    if filepath is None:
        filepath = os.path.join(
            os.path.dirname(__file__),
            "crime/01_District_wise_crimes_committed_IPC_2001_2012.csv",
        )
    return pd.read_csv(filepath)


def filter_and_aggregate(df):
    filtered = df[(df["DISTRICT"] != "TOTAL") & (df["YEAR"] == 2012)]
    aggregated = (
        filtered.groupby("STATE/UT")["TOTAL IPC CRIMES"].sum().reset_index()
    )
    return aggregated


def get_top_states(agg_df, n=5):
    return agg_df.sort_values(by="TOTAL IPC CRIMES", ascending=False).head(n)


def main():
    df = load_data()
    agg_df = filter_and_aggregate(df)
    top_states = get_top_states(agg_df, 5)
    print(top_states)


if __name__ == "__main__":
    main()
