import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

# read data from CSV file
df = pd.read_csv('aft.csv')

# create a Flask app
app = Flask(__name__)

# define a route for the web page
@app.route('/')
def index():
    # render the template with the data from the CSV file
    return render_template('index.html', data=df.to_html())

if __name__ == '__main__':
    # run the app on port 8000
    app.run(debug=True, host='0.0.0.0', port=8000)
