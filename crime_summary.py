import os
import pandas as pd


def load_data():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(
        base_dir, 'crime', '01_District_wise_crimes_committed_IPC_2001_2012.csv'
    )
    return pd.read_csv(csv_path)


def top_states(df=None):
    if df is None:
        df = load_data()
    total_df = df[df['DISTRICT'] == 'TOTAL']
    state_totals = total_df.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum()
    top_10 = state_totals.nlargest(10)
    print(top_10)


def yearly_totals(df=None):
    if df is None:
        df = load_data()
    total_df = df[df['DISTRICT'] == 'TOTAL']
    year_totals = total_df.groupby('YEAR')['TOTAL IPC CRIMES'].sum()
    print(year_totals)


if __name__ == '__main__':
    df = load_data()
    top_states(df)
    yearly_totals(df)
