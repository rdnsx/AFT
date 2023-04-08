### AFT - Aquarium Fertilizer Tracker  

This code prompts the user to enter daily fertilizer doses for an aquarium and stores the data in a pandas dataframe. It then plots a graph of the fertilizer doses over time and saves the data to a CSV file.

The while loop allows the user to continue entering data until they choose to stop.

The plot function of pandas is used to plot the graph, with the date on the x-axis and the three different fertilizer doses on the y-axis. The plot is then given a title, x-label, and y-label using the matplotlib.pyplot library. Finally, the plot is displayed using the plt.show() function.

The data is then saved to a CSV file using the to_csv method of pandas dataframe, with the index set to false to exclude the index column.

Note that the code assumes that the user will enter valid input (i.e., the date is in the correct format, and the doses are entered as floats). It may be useful to include error handling to prevent the code from crashing if invalid input is entered.