import pandas as pd


def load_crime_data(filepath='crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'):
    """Load district-wise IPC crimes CSV using pandas."""
    return pd.read_csv(filepath)


def process_crime_data(df):
    """Drop rows where DISTRICT is 'TOTAL' and keep rows where YEAR is 2012."""
    filtered_df = df[(df['DISTRICT'] != 'TOTAL') & (df['YEAR'] == 2012)]
    return filtered_df


def get_top_states_by_crime(df, top_n=5):
    """Group by STATE/UT, sum TOTAL IPC CRIMES, and return top states/UTs."""
    state_totals = df.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum()
    return state_totals.nlargest(top_n)


def main():
    df = load_crime_data()
    filtered_df = process_crime_data(df)
    top_states = get_top_states_by_crime(filtered_df, top_n=5)
    print(top_states)


if __name__ == '__main__':
    main()
