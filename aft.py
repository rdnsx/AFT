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
date = input('Enter the date (DD-MM-YYYY): ')
eisen = float(input('Enter the Fe dose: '))
phosphat = float(input('Enter the PO4 dose: '))
nitrat = float(input('Enter the NO3 dose: '))

# Add input to DataFrame
df = pd.concat([df, pd.DataFrame({'date': date, 'eisen': eisen, 'phosphat': phosphat, 'nitrat': nitrat}, index=[0])], ignore_index=True)

# Write DataFrame to CSV file
df.to_csv(csv_file, index=False)

