import os
import pandas as pd

def print_district_count_2012():
    csv_path = os.path.join(os.path.dirname(__file__), 'crime', '01_District_wise_crimes_committed_IPC_2001_2012.csv')
    df = pd.read_csv(csv_path)
    filtered = df[(df['YEAR'] == 2012) & (df['DISTRICT'] != 'TOTAL')]
    print(filtered['DISTRICT'].nunique())

if __name__ == '__main__':
    print_district_count_2012()
