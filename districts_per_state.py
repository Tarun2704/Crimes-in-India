import pandas as pd

def load_and_process_data(file_path):
    """
    Loads the crime data, filters for the year 2012, and drops rows where DISTRICT is 'TOTAL'.
    """
    df = pd.read_csv(file_path)
    df_filtered = df[df['YEAR'] == 2012]
    df_cleaned = df_filtered[df_filtered['DISTRICT'] != 'TOTAL']
    return df_cleaned

def print_districts_per_state(df):
    """
    Groups the DataFrame by 'STATE/UT', counts unique districts, and prints the results
    sorted in descending order of district count.
    """
    districts_count = df.groupby('STATE/UT')['DISTRICT'].nunique().sort_values(ascending=False)
    print("Number of districts per STATE/UT (Year 2012, excluding 'TOTAL' district):")
    print(districts_count)

if __name__ == '__main__':
    file_path = 'crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'
    processed_df = load_and_process_data(file_path)
    print_districts_per_state(processed_df)
