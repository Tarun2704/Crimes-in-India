import pandas as pd
import os

# Path to the CSV file
csv_file_path = os.path.join('crime', '01_District_wise_crimes_committed_IPC_2001_2012.csv')

# Load the CSV file
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found. Please ensure it's in the correct directory.")
    exit()

# Filter rows where DISTRICT is 'TOTAL'
total_crimes_df = df[df['DISTRICT'] == 'TOTAL']

# Sum 'TOTAL IPC CRIMES' per 'YEAR'
crimes_by_year = total_crimes_df.groupby('YEAR')['TOTAL IPC CRIMES'].sum()

# Get the top 5 years with the highest totals
top_5_years = crimes_by_year.nlargest(5)

# Print the top 5 years and their corresponding crime totals
print("Top 5 crime years:")
for year, total_crimes in top_5_years.items():
    print(f"Year: {int(year)}, Total IPC Crimes: {total_crimes}")
