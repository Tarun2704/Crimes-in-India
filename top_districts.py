import pandas as pd

def load_crime_data(file_path):
    """
    Loads crime data from a CSV file, filters out 'TOTAL' districts,
    and keeps only data for the year 2012.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A filtered DataFrame containing crime data.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return pd.DataFrame()

    # Clean column names by stripping whitespace
    df.columns = df.columns.str.strip()

    # Filter out rows where DISTRICT is 'TOTAL'
    df_filtered = df[df['DISTRICT'] != 'TOTAL']

    # Keep only data for the year 2012
    df_2012 = df_filtered[df_filtered['YEAR'] == 2012]

    return df_2012

def get_top_districts(df, num_districts=10):
    """
    Sorts the DataFrame by 'TOTAL IPC CRIMES' and returns the top N districts.

    Args:
        df (pd.DataFrame): The input DataFrame.
        num_districts (int): The number of top districts to retrieve.

    Returns:
        pd.DataFrame: A DataFrame containing the top N districts.
    """
    # Ensure 'TOTAL IPC CRIMES' column exists and is numeric
    if 'TOTAL IPC CRIMES' not in df.columns:
        print("Error: 'TOTAL IPC CRIMES' column not found in the DataFrame.")
        return pd.DataFrame()
    
    df['TOTAL IPC CRIMES'] = pd.to_numeric(df['TOTAL IPC CRIMES'], errors='coerce')
    df_sorted = df.sort_values(by='TOTAL IPC CRIMES', ascending=False)
    return df_sorted.head(num_districts)

def print_results(df_top_districts):
    """
    Prints the 'STATE/UT', 'DISTRICT', and 'TOTAL IPC CRIMES' for the given DataFrame.

    Args:
        df_top_districts (pd.DataFrame): DataFrame with top districts data.
    """
    if df_top_districts.empty:
        print("No data to display.")
        return

    print("Top 10 Districts with Most 'TOTAL IPC CRIMES' in 2012:")
    for index, row in df_top_districts.iterrows():
        print(f"STATE/UT: {row['STATE/UT']}, DISTRICT: {row['DISTRICT']}, TOTAL IPC CRIMES: {row['TOTAL IPC CRIMES']}")

if __name__ == '__main__':
    file_path = 'crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'
    
    # Load and filter data
    crime_data_2012 = load_crime_data(file_path)

    if not crime_data_2012.empty:
        # Get top districts
        top_districts = get_top_districts(crime_data_2012)
        
        # Print results
        print_results(top_districts)
