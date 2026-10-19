import pandas as pd

def main():
    df = pd.read_csv('crime/01_District_wise_crimes_committed_IPC_2001_2012.csv')
    df_2012 = df[df['YEAR'] == 2012]
    filtered = df_2012[df_2012['DISTRICT'].str.upper() != 'TOTAL']
    print(filtered['DISTRICT'].nunique())

if __name__ == '__main__':
    main()
