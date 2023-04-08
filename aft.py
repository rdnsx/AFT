import pandas as pd
import os.path
from os import path

csv_file = 'data.csv'

# Check if CSV file exists
if path.exists(csv_file):
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame(columns=['date', 'eisen', 'phosphat', 'nitrat'])

# Get user input
date = input('Enter the date (DD.MM.YYYY): ')
eisen = input('Enter the Fe dose (drops): ')
phosphat = input('Enter the Phosphat dose (ml): ')
nitrat = input('Enter the Nitrat dose (ml): ')

# Add input to DataFrame
df = df.append({'date': date, 'eisen': eisen, 'phosphat': phosphat, 'nitrat': nitrat}, ignore_index=True)

# Write DataFrame to CSV file
df.to_csv(csv_file, index=False)
