import pandas as pd


def load_data(filepath='crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'):
    """Load the CSV dataset using pandas with a relative path."""
    return pd.read_csv(filepath)


def filter_total_districts(df):
    """Filter rows where DISTRICT is 'TOTAL'."""
    return df[df['DISTRICT'] == 'TOTAL']


def aggregate_and_compute_change(df):
    """Aggregate total IPC crimes per year and compute percentage change from previous year."""
    agg_df = df.groupby('YEAR')['TOTAL IPC CRIMES'].sum().reset_index()
    agg_df['PERCENTAGE_CHANGE'] = agg_df['TOTAL IPC CRIMES'].pct_change() * 100
    return agg_df


def print_crime_trend(df):
    """Print each year with its total crimes and percentage change."""
    for _, row in df.iterrows():
        year = int(row['YEAR'])
        total = row['TOTAL IPC CRIMES']
        pct_change = row['PERCENTAGE_CHANGE']
        change_str = f"{pct_change:.2f}%" if pd.notna(pct_change) else "N/A"
        print(f"Year: {year} | Total IPC Crimes: {total:,} | Percentage Change: {change_str}")


def print_biggest_increase(df):
    """Print the year with the biggest percentage increase."""
    valid_df = df.dropna(subset=['PERCENTAGE_CHANGE'])
    if not valid_df.empty:
        max_row = valid_df.loc[valid_df['PERCENTAGE_CHANGE'].idxmax()]
        year = int(max_row['YEAR'])
        pct_change = max_row['PERCENTAGE_CHANGE']
        print(f"\nYear with the biggest percentage increase: {year} ({pct_change:.2f}%)")


def main():
    df = load_data()
    filtered_df = filter_total_districts(df)
    trend_df = aggregate_and_compute_change(filtered_df)
    print_crime_trend(trend_df)
    print_biggest_increase(trend_df)


if __name__ == '__main__':
    main()
