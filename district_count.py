import pandas as pd


def count_districts():
    df = pd.read_csv("crime/01_District_wise_crimes_committed_IPC_2001_2012.csv")
    filtered = df[(df["YEAR"] == 2012) & (df["DISTRICT"] != "TOTAL")]
    print(filtered["DISTRICT"].nunique())


if __name__ == "__main__":
    count_districts()
