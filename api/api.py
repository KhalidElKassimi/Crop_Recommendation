from flask import Flask, jsonify
import pandas as pd
import time

app = Flask(__name__)

# Load your CSV file
csv_file_path = 'cropmetrics.csv'
df = pd.read_csv(csv_file_path)

# Initialize counter
current_line = 0

# Endpoint to get data in batches
@app.route('/get_data', methods=['GET'])
def get_data():
    global current_line
    start=current_line
    end=current_line+5
    current_line= end if end < len(df) else 0
    data_batch = df.iloc[start:end].to_dict(orient='records')

    # Simulate a delay of one minute
    time.sleep(60)

    return jsonify(data_batch)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)