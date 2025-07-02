from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and columns
model = pickle.load(open('bengaluru_home_prices_model.pickle', 'rb'))

columns = json.load(open('columns.json', 'r'))['data_columns']  # includes location columns
X_columns = columns

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = X_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(X_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

# Wrap in DataFrame with proper column names
    x_df = pd.DataFrame([x], columns=X_columns)
    return round(model.predict(x_df)[0], 2)

@app.route('/')
def index():
    locations = [col.title() for col in X_columns[3:]]  # skip sqft, bath, bhk
    return render_template('index.html', locations=sorted(locations))

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    sqft = float(request.form['sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    predicted_price = predict_price(location, sqft, bath, bhk)
    return render_template('index.html', prediction_text=f"Estimated Price: ₹ {predicted_price} Lakhs", locations=sorted([col.title() for col in X_columns[3:]]))

if __name__ == '__main__':
    app.run(debug=True)  # or debug=False for production
