import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def filter_data(df):
    filtered = df[(df['DISTRICT'] != 'TOTAL') & (df['YEAR'] == 2012)]
    return filtered

def print_top_districts(df):
    top_10 = df.nlargest(10, 'TOTAL IPC CRIMES')
    for _, row in top_10.iterrows():
        print(f"District: {row['DISTRICT']}, State/UT: {row['STATE/UT']}, Total IPC Crimes: {row['TOTAL IPC CRIMES']}")

def print_bottom_districts(df):
    bottom_5 = df.nsmallest(5, 'TOTAL IPC CRIMES')
    for _, row in bottom_5.iterrows():
        print(f"District: {row['DISTRICT']}, State/UT: {row['STATE/UT']}, Total IPC Crimes: {row['TOTAL IPC CRIMES']}")

if __name__ == '__main__':
    filepath = 'crime/01_District_wise_crimes_committed_IPC_2001_2012.csv'
    df = load_data(filepath)
    filtered_df = filter_data(df)
    print("Top 10 Districts:")
    print_top_districts(filtered_df)
    print("\nBottom 5 Districts:")
    print_bottom_districts(filtered_df)
