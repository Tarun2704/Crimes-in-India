import pandas as pd
import os

def load_data(file_path):
    """
    Loads the crime data from the given CSV file and filters for 'TOTAL' districts.
    """
    df = pd.read_csv(file_path)
    # Keep only rows where DISTRICT == 'TOTAL' (these are the state totals)
    df_total = df[df['DISTRICT'] == 'TOTAL'].copy()
    return df_total

def top_states(df):
    """
    Prints the top 10 states by the sum of 'TOTAL IPC CRIMES' across all years.
    """
    # Sum 'TOTAL IPC CRIMES' for each state across all years
    state_crime_totals = df.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().nlargest(10)
    print("Top 10 states by total IPC crimes (all years):")
    print(state_crime_totals)
    print("\n")

def yearly_totals(df):
    """
    Prints the total 'TOTAL IPC CRIMES' for each 'YEAR'.
    """
    # Sum 'TOTAL IPC CRIMES' for each year
    yearly_crime_totals = df.groupby('YEAR')['TOTAL IPC CRIMES'].sum()
    print("Total IPC crimes for each year:")
    print(yearly_crime_totals)
    print("\n")

if __name__ == '__main__':
    # Construct the path to the CSV file relative to the script's directory
    script_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(script_dir, 'crime', '01_District_wise_crimes_committed_IPC_2001_2012.csv')

    # Load data
    df_filtered = load_data(csv_file_path)

    # Print top states
    top_states(df_filtered)

    # Print yearly totals
    yearly_totals(df_filtered)
