
# 🏠 House Price Prediction System

This project is a simple **Machine Learning-based House Price Prediction System** developed using Python. It uses **Linear Regression** to predict the price of a house based on two main features: **house area in square feet** and **number of bedrooms**.

## 📌 Project Overview

The model is trained using a sample house price dataset containing information about:

* Area of the house (sqft)
* Number of bedrooms
* House price

After training the Linear Regression model, the user can enter the area and number of bedrooms, and the system predicts the estimated house price.

## ⚙️ Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn
* Linear Regression
* R² Score

## 🔄 Working Process

1. Create and load the house price dataset.
2. Convert the data into a Pandas DataFrame.
3. Separate input features and target price.
4. Split the dataset into training and testing data.
5. Train a Linear Regression model.
6. Evaluate the model using the R² score.
7. Take house area and bedroom count from the user.
8. Predict the estimated house price.
9. Display a graph showing the actual data and regression line.

## 🧠 Machine Learning Model

**Algorithm:** Linear Regression

**Input Features:**

* `Area_sqft`
* `Bedrooms`

**Target:**

* `Price`

## 📊 Output

The system displays:

* House price dataset
* R² score
* Predicted house price
* House price prediction graph

### Example

```text
Enter House Area (sqft): 1800
Enter Number of Bedrooms: 3

Predicted House Price: ₹5,XXX,XXX.XX
```

## 🎯 Objective

The main objective of this project is to understand and demonstrate how **Linear Regression can be used to predict house prices from property-related features**.

## 📁 Project Type

**Machine Learning / Data Science Mini Project**
