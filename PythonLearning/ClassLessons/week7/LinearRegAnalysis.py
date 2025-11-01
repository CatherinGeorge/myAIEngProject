# linear_regression_sales.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1️ Load the dataset
df = pd.read_csv(r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\ClassLessons\week7\salary.csv")
print("Dataset loaded successfully!")
print(df.head(), "\n")

# 2️ Check for missing values
print("Missing values in each column:\n", df.isnull().sum(), "\n")

# Assuming the dataset has columns like "YearsExperience" and "Salary"
X = df.iloc[:, :-1].values   # Independent variable(s)
y = df.iloc[:, -1].values    # Dependent variable (target)

# 3 Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Data split completed:")
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}\n")

# 4️ Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("Model training completed!\n")

# 5️ Predict using the trained model
y_pred = model.predict(X_test)

# 6️ Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Metrics:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score (R²): {r2:.2f}\n")

# 7️ Visualization: Plotting the regression line
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color="blue", label="Actual Data")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Regression Line")
plt.title("Linear Regression: Actual vs Predicted")
plt.xlabel("Experience / Sales / Independent Variable")
plt.ylabel("Salary / Dependent Variable")
plt.legend()
plt.show()

# 8️ Print model parameters
print("Intercept (b₀):", model.intercept_)
print("Coefficient (b₁):", model.coef_)
