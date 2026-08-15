import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

Data = {
    "Area_sqft": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    "Bedrooms": [1, 2, 2, 3, 3, 4, 4, 4, 5, 5],
    "Price": [2000000, 2800000, 3500000, 4500000, 5500000,
              6500000, 7200000, 8000000, 9000000, 9800000]
}

df = pd.DataFrame(Data)

print("House Price Dataset")
print(df)

x = df[["Area_sqft", "Bedrooms"]]    #features(input)
y = df["Price"]    #target(output)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(x_train, y_train)

pred = model.predict(x_test)     # Prediction on test data

score = r2_score(y_test, pred)    #accuracy

print("\nR2 Score:", score)
print("Accuracy (R2 Score):", round(score, 4))

# User Input
area = float(input("\nEnter House Area (sqft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))

prediction = model.predict([[area, bedrooms]])

print(f"\nPredicted House Price: ₹{prediction[0]:,.2f}")

# Graph
plt.figure(figsize=(8,5))

plt.scatter(df["Area_sqft"], df["Price"],
            color="blue", label="Actual Data")

# Regression Line
plt.plot(df["Area_sqft"], model.predict(x),
         color="red", label="Regression Line")

plt.title("House Price Prediction")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.savefig("house price prediction system.png")
plt.show()