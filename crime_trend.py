import pandas as pd

def load_data(file_path='crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'):
    """Load crime data CSV using pandas."""
    return pd.read_csv(file_path)

def process_data(df):
    """Filter rows where DISTRICT == 'TOTAL' and sum TOTAL IPC CRIMES per YEAR."""
    filtered_df = df[df['DISTRICT'] == 'TOTAL']
    grouped_df = filtered_df.groupby('YEAR')['TOTAL IPC CRIMES'].sum().reset_index()
    return grouped_df

def calculate_percentage_change(df):
    """Compute percentage change of total IPC crimes from the previous year."""
    df = df.copy()
    df['PERCENT_CHANGE'] = df['TOTAL IPC CRIMES'].pct_change() * 100
    return df

def print_trends(df):
    """Print each year, its total crimes, and percentage change."""
    for _, row in df.iterrows():
        year = int(row['YEAR'])
        total = int(row['TOTAL IPC CRIMES'])
        pct_change = row['PERCENT_CHANGE']
        
        if pd.isna(pct_change):
            pct_str = 'N/A'
        else:
            pct_str = f"{pct_change:.2f}%"
            
        print(f"Year: {year} | Total IPC Crimes: {total} | Percentage Change: {pct_str}")

def print_biggest_increase(df):
    """Identify and print the year with the biggest increase."""
    valid_df = df.dropna(subset=['PERCENT_CHANGE'])
    if not valid_df.empty:
        max_row = valid_df.loc[valid_df['PERCENT_CHANGE'].idxmax()]
        year = int(row['YEAR'])
        pct_change = max_row['PERCENT_CHANGE']
        print(f"\nYear with the biggest increase: {year} ({pct_change:.2f}%)")

if __name__ == '__main__':
    data = load_data()
    processed = process_data(data)
    with_change = calculate_percentage_change(processed)
    print_trends(with_change)
    print_biggest_increase(with_change)
