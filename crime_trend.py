import os
import pandas as pd

def load_data():
    """Load the district-wise crimes CSV using a path relative to the script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(
        script_dir,
        'crime',
        '01_District_wise_crimes_committed_IPC_2001_2012.csv'
    )
    return pd.read_csv(csv_path)

def process_data(df):
    """Filter rows where DISTRICT == 'TOTAL', group by YEAR, sum 'TOTAL IPC CRIMES', and calculate percentage change."""
    filtered = df[df['DISTRICT'] == 'TOTAL']
    grouped = filtered.groupby('YEAR')['TOTAL IPC CRIMES'].sum().reset_index()
    grouped['PERCENTAGE_CHANGE'] = grouped['TOTAL IPC CRIMES'].pct_change() * 100
    return grouped

def print_trends(grouped_df):
    """Print each year with its total and percentage change from the previous year."""
    for _, row in grouped_df.iterrows():
        year = int(row['YEAR'])
        total = row['TOTAL IPC CRIMES']
        pct_change = row['PERCENTAGE_CHANGE']
        if pd.isna(pct_change):
            change_str = "N/A"
        else:
            change_str = f"{pct_change:.2f}%"
        print(f"Year: {year} | Total IPC Crimes: {total} | Percentage Change: {change_str}")

def print_biggest_increase(grouped_df):
    """Print the year with the biggest increase in total IPC crimes."""
    valid_df = grouped_df.dropna(subset=['PERCENTAGE_CHANGE'])
    if not valid_df.empty:
        max_row = valid_df.loc[valid_df['PERCENTAGE_CHANGE'].idxmax()]
        year = int(max_row['YEAR'])
        pct_change = max_row['PERCENTAGE_CHANGE']
        print(f"\nYear with the biggest increase: {year} ({pct_change:.2f}%)")

def print_average_change(grouped_df):
    """Print the average yearly percentage change in total IPC crimes."""
    avg_change = grouped_df['PERCENTAGE_CHANGE'].mean()
    if not pd.isna(avg_change):
        print(f"Average yearly change: {avg_change:.2f}%")

if __name__ == '__main__':
    df = load_data()
    grouped_df = process_data(df)
    print_trends(grouped_df)
    print_biggest_increase(grouped_df)
    print_average_change(grouped_df)
