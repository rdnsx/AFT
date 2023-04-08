import pandas as pd
import matplotlib.pyplot as plt

# define the name of the CSV file
csv_file = 'aft.csv'

# create an empty dataframe to store the fertilizer dose or load the existing one
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Date', 'Fe drops', 'PO4 ml', 'NO3 ml'])

# set the 'Date' column as the index
df = df.set_index('Date')

while True:
    # get the date and fertilizer dose from the user
    date = input('Enter the date (DD.MM.YYYY): ')

    # check if the date already exists in the index
    if date in df.index:
        print('Data for this date already exists. Please enter a different date.')
        continue

    fe = float(input('Enter the Fe dose(drops): '))
    po4 = float(input('Enter the PO4 dose (ml): '))
    no3 = float(input('Enter the NO3 dose (ml): '))

    # append the data to the dataframe
    df.loc[date] = [fe, po4, no3]

    # ask the user if they want to continue entering data
    choice = input('Do you want to enter another dose (y/n)? ')
    if choice.lower() == 'n':
        break

# plot the graph
df.plot()
plt.title('Daily Aquarium Fertilizer Dose')
plt.xlabel('Date')
plt.ylabel('Fertilizer Dose')
plt.show()

# reset the index to the default integer index
df = df.reset_index()

# save the data to the CSV file
df.to_csv(csv_file, mode='w', index=False, header=True)
