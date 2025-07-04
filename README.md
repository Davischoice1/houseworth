# 🏠 Bengaluru House Price Prediction

This project is a machine learning-based web application that predicts house prices in Bengaluru, India, based on input features like location, square footage, number of bedrooms, bathrooms, and more.

## 📌 Problem Definition

Predicting house prices accurately helps buyers, sellers, and real estate professionals make informed decisions. This regression problem uses various housing features to estimate market value.

## 📊 Dataset

- **Source**: Kaggle - [Bengaluru House Price Data](https://www.kaggle.com/datasets)
- **Size**: ~13,000 rows, 9 columns
- **Format**: CSV

## ⚙️ Features Used

- `location`: Area or neighborhood
- `total_sqft`: Total square footage of the property
- `bath`: Number of bathrooms
- `bhk`: Number of bedrooms
- `price_per_sqft`: Engineered feature
- `availability`: Property availability status
- `area_type`: Super built-up, plot, etc.

## 🧹 Data Preprocessing

- Removed outliers and missing values
- Converted `total_sqft` strings to numeric values
- Encoded categorical variables (e.g., location)
- Created new features like `price_per_sqft`
- Scaled numerical features using `StandardScaler`

## 🤖 Model Building

Three regression models were trained and evaluated:
1. **Linear Regression** – baseline model
2. **Random Forest Regressor** – ensemble learning
3. **Gradient Boosting Regressor** – performance-focused

## 🧪 Model Evaluation

| Model                    | R² Score |
|--------------------------|----------|
| Linear Regression        | 0.84     |
| Random Forest Regressor | 0.91     |
| Gradient Boosting       | 0.93     |

> Best performance: ✅ **Gradient Boosting Regressor**

## 🌐 Web App (Flask)

A Flask web interface allows users to:
- Enter housing details
- Select location, size, and other features
- Get a **predicted price** instantly

### Screenshots

![Prediction Form](screenshots/form.png)
![Prediction Output](screenshots/output.png)

## 🚀 How to Run Locally

--- bash
# Clone the repository
git clone https://github.com/Davischoice1/houseworth.git
cd house_price_prediction

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # or venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
