import pandas as pd
import argparse
import os

def load_data(file_path):
    """
    Loads the crime data from the specified CSV file.
    """
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file_path)
    return pd.read_csv(abs_file_path)

def filter_data(df, state_name):
    """
    Filters the DataFrame for the given state and 'TOTAL' district.
    """
    filtered_df = df[(df['STATE/UT'] == state_name) & (df['DISTRICT'] == 'TOTAL')]
    return filtered_df

def print_crimes_per_year(df):
    """
    Prints the year and total IPC crimes for each row in the DataFrame.
    """
    for index, row in df.iterrows():
        print(f"YEAR: {int(row['YEAR'])}, TOTAL IPC CRIMES: {int(row['TOTAL IPC CRIMES'])}")

def main():
    parser = argparse.ArgumentParser(description="Calculate crimes per year for a given state.")
    parser.add_argument('--state', type=str, default='KERALA',
                        help="Name of the state/UT to filter (default: KERALA)")
    args = parser.parse_args()

    file_path = 'crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'
    
    try:
        df = load_data(file_path)
        filtered_df = filter_data(df, args.state)
        if filtered_df.empty:
            print(f"No data found for state: {args.state} with DISTRICT == 'TOTAL'")
        else:
            print(f"Crimes per year for {args.state} (DISTRICT == 'TOTAL'):")
            print_crimes_per_year(filtered_df)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Make sure the script is run from the repository root.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
