import pandas as pd
import matplotlib.pyplot as plt

# define the name of the CSV file
csv_file = 'aft.csv'

# create an empty dataframe to store the fertilizer dose or load the existing one
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['date', 'eisen', 'phosphat', 'nitrat'])

while True:
    # get the date and fertilizer dose from the user
    date = input('Enter the date (DD.MM.YYYY): ')
    eisen = float(input('Enter the Fe dose(drops): '))
    phosphat = float(input('Enter the PO4 dose (ml): '))
    nitrat = float(input('Enter the NO3 dose (ml): '))
    
    # append the data to the dataframe
    df = pd.concat([df, pd.DataFrame({'date': date, 'eisen': eisen, 'phosphat': phosphat, 'nitrat': nitrat}, index=[0])], ignore_index=True)
    
    # ask the user if they want to continue entering data
    choice = input('Do you want to enter another dose (y/n)? ')
    if choice.lower() == 'n':
        break

# plot the graph
df.plot(x='Datum', y=['Fe', 'PO4', 'NO3'])
plt.title('Daily Aquarium Fertilizer Dose')
plt.xlabel('Date')
plt.ylabel('Fertilizer Dose')
plt.show()

# save the data to the CSV file
df.to_csv(csv_file, mode='a', index=False, header=not df.index.any())
