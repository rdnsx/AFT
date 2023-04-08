import pandas as pd
import matplotlib.pyplot as plt

# create an empty dataframe to store the fertilizer dose
df = pd.DataFrame(columns=['date', 'eisen', 'phosphat', 'nitrat'])

while True:
    # get the date and fertilizer dose from the user
    date = input('Enter the date (YYYY-MM-DD): ')
    eisen = float(input('Enter the Eisen dose: '))
    phosphat = float(input('Enter the Phosphat dose: '))
    nitrat = float(input('Enter the Nitrat dose: '))
    
    # append the data to the dataframe
    df = df.append({'date': date, 'eisen': eisen, 'phosphat': phosphat, 'nitrat': nitrat}, ignore_index=True)
    
    # ask the user if they want to continue entering data
    choice = input('Do you want to enter another dose (y/n)? ')
    if choice.lower() == 'n':
        break

# plot the graph
df.plot(x='date', y=['eisen', 'phosphat', 'nitrat'])
plt.title('Daily Aquarium Fertilizer Dose')
plt.xlabel('Date')
plt.ylabel('Fertilizer Dose')
plt.show()

# save the data to a CSV file
df.to_csv('aquarium_fertilizer_dose.csv', index=False)
