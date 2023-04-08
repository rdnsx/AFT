from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    # Get user input
    date = request.form['date']
    eisen = float(request.form['eisen'])
    phosphat = float(request.form['phosphat'])
    nitrat = float(request.form['nitrat'])

    csv_file = 'data.csv'

    # Check if CSV file exists
    if path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['date', 'eisen', 'phosphat', 'nitrat'])

    # Add input to DataFrame
    df = pd.concat([df, pd.DataFrame({'date': date, 'eisen': eisen, 'phosphat': phosphat, 'nitrat': nitrat}, index=[0])], ignore_index=True)

    # Write DataFrame to CSV file
    df.to_csv(csv_file, index=False)

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
