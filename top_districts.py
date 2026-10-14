import pandas as pd
import os

def load_data(filepath):
    return pd.read_csv(filepath)

def get_top_districts(df):
    filtered = df[(df['YEAR'] == 2012) & (df['DISTRICT'] != 'TOTAL')]
    sorted_df = filtered.sort_values(by='TOTAL IPC CRIMES', ascending=False)
    return sorted_df.head(10)[['STATE/UT', 'DISTRICT', 'TOTAL IPC CRIMES']]

def get_bottom_districts(df):
    filtered = df[(df['YEAR'] == 2012) & (df['DISTRICT'] != 'TOTAL')]
    sorted_df = filtered.sort_values(by='TOTAL IPC CRIMES', ascending=True)
    return sorted_df.head(5)[['STATE/UT', 'DISTRICT', 'TOTAL IPC CRIMES']]

def main():
    filepath = os.path.join('crime', '01_District_wise_crimes_committed_IPC_2001_2012.csv')
    df = load_data(filepath)
    top_10 = get_top_districts(df)
    print(top_10)
    print("\nBottom 5 districts:")
    bottom_5 = get_bottom_districts(df)
    print(bottom_5)

if __name__ == '__main__':
    main()
