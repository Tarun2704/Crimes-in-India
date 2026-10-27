import os
import pandas as pd

def count_districts_2012():
    csv_path = os.path.join(
        os.path.dirname(__file__),
        'crime',
        '01_District_wise_crimes_committed_IPC_2001_2012.csv'
    )
    df = pd.read_csv(csv_path)
    filtered_df = df[(df['YEAR'] == 2012) & (df['DISTRICT'] != 'TOTAL')]
    district_count = filtered_df['DISTRICT'].nunique()
    print(district_count)

if __name__ == '__main__':
    count_districts_2012()
