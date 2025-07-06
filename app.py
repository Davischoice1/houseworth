from flask import Flask, request, render_template
import pickle
import json
import numpy as np
import os


app = Flask(__name__)

# Load model and columns
model = pickle.load(open('bengaluru_home_prices_model.pickle', 'rb'))
columns = json.load(open('columns.json', 'r'))['data_columns']
X_columns = columns

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = X_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(X_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

@app.route('/')
def index():
    locations = sorted([col.title() for col in X_columns[3:]])  # skip sqft, bath, bhk
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        location = request.form['location']
        sqft = float(request.form['sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])

        predicted_price = predict_price(location, sqft, bath, bhk)
        price_str = f"Estimated Price: ₹ {predicted_price:,.2f} Lakhs"

        locations = sorted([col.title() for col in X_columns[3:]])
        return render_template('index.html', prediction_text=price_str, locations=locations)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", locations=sorted([col.title() for col in X_columns[3:]]))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

