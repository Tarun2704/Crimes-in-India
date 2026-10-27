import pandas as pd
import os

# Define the absolute path to the crime directory
CRIME_DIR = os.path.join(os.path.dirname(__file__), 'crime')

# Define the list of CSV file paths
csv_files = [
    os.path.join(CRIME_DIR, '01_District_wise_crimes_committed_IPC_2001_2012.csv'),
    os.path.join(CRIME_DIR, '01_District_wise_crimes_committed_IPC_2013.csv'),
    os.path.join(CRIME_DIR, '01_District_wise_crimes_committed_IPC_2014.csv')
]

all_crimes_df = pd.DataFrame()

for file_path in csv_files:
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Filter out rows where 'DISTRICT' is "TOTAL" or ends with "TOTAL"
    # The regex 'TOTAL$' matches "TOTAL" at the end of the string, which covers both "TOTAL" and "DISTRICT TOTAL"
    df_filtered = df[~df['DISTRICT'].str.contains('TOTAL$', regex=True, na=False)]

    # Select 'YEAR' and 'TOTAL IPC CRIMES' columns
    df_selected = df_filtered[['YEAR', 'TOTAL IPC CRIMES']]

    # Append to the master DataFrame
    all_crimes_df = pd.concat([all_crimes_df, df_selected], ignore_index=True)

# Group by 'YEAR' and sum 'TOTAL IPC CRIMES'
yearly_totals = all_crimes_df.groupby('YEAR')['TOTAL IPC CRIMES'].sum()

# Sort the results by 'YEAR' in ascending order
yearly_totals_sorted = yearly_totals.sort_index(ascending=True)

# Print one line per year, oldest first
for year, total_crimes in yearly_totals_sorted.items():
    print(f"{year}: {total_crimes:,}")
