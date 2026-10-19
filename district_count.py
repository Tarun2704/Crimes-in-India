import pandas as pd

df = pd.read_csv('crime/01_District_wise_crimes_committed_IPC_2001_2012.csv')
filtered = df[(df['YEAR'] == 2012) & (df['DISTRICT'] != 'TOTAL')]
count = filtered['DISTRICT'].nunique()
print(count)
