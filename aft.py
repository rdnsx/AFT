import pandas as pd
import matplotlib.pyplot as plt
import http.server
import socketserver
import threading

# define the name of the CSV file and the directory to serve
csv_file = '/app/aft.csv'
static_dir = 'static'

# create an empty dataframe to store the fertilizer dose or load the existing one
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['date', 'eisen', 'phosphat', 'nitrat'])

# define the request handler for the web server
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # show the HTML file that displays the CSV data
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# define a function to start the web server in a separate thread
def start_web_server():
    with socketserver.TCPServer(("", 8000), MyHttpRequestHandler) as httpd:
        print('Web server started at http://localhost:8000')
        httpd.serve_forever()

# start the web server in a separate thread
threading.Thread(target=start_web_server).start()

while True:
    # get the date and fertilizer dose from the user
    date = input('Enter the date (DD-MM-YYYY): ')
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
df.plot(x='date', y=['eisen', 'phosphat', 'nitrat'])
plt.title('Daily Aquarium Fertilizer Dose')
plt.xlabel('Date')
plt.ylabel('Fertilizer Dose')
plt.savefig(f"{static_dir}/plot.png")

# save the data to the CSV file
df.to_csv(csv_file, mode='a', index=False, header=not df.index.any())
