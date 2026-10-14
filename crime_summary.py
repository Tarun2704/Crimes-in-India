import pandas as pd
import os

def load_data(file_path):
    """
    Loads the crime data from a CSV file into a pandas DataFrame.
    """
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_path)
    df = pd.read_csv(abs_file_path)
    return df

def top_states(df):
    """
    Prints the top 10 states by the sum of 'TOTAL IPC CRIMES' across all years.
    """
    state_totals = df[df['DISTRICT'] == 'TOTAL'].groupby('STATE/UT')['TOTAL IPC CRIMES'].sum()
    top_10_states = state_totals.nlargest(10)
    print("Top 10 States by Total IPC Crimes (2001-2012):")
    print(top_10_states)
    print("\n")

def yearly_totals(df):
    """
    Prints the total 'TOTAL IPC CRIMES' for each 'YEAR'.
    """
    yearly_crime_totals = df.groupby('YEAR')['TOTAL IPC CRIMES'].sum()
    print("Total IPC Crimes per Year:")
    print(yearly_crime_totals)
    print("\n")

if __name__ == '__main__':
    csv_file = 'crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'
    
    try:
        crime_df = load_data(csv_file)
        top_states(crime_df)
        yearly_totals(crime_df)
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found. Please ensure it's in the correct path relative to the script.")
    except KeyError as e:
        print(f"Error: A required column was not found in the CSV. Please check column names. Missing: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
