# Home Assignment <4> - Predicting House Prices using Regression
# ---------------------------------------------------------------
# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the dataset
df = pd.read_csv(r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\HomeAssigments\Wk7AIAssignments\house_price_regression_dataset.csv")

# Show raw column names
print("Original columns:")
for col in df.columns:
    print(f"'{col}'")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "").str.lower()
print("Cleaned columns:", df.columns.tolist())

# Now access by cleaned names
df = df[['squarefeet', 'price']]

print(df.head())

# Step 2: Exploratory Data Analysis (EDA)
print("\n===== First Five Rows =====")
print(df.head())

print("\n===== Missing Values =====")
print(df.isnull().sum())

# Handle missing values (if any)
df = df.dropna()

# Scatter plot: Square Footage vs Price
plt.figure(figsize=(7, 5))
plt.scatter(df['squarefeet'], df['price'], color='blue', alpha=0.6)
plt.title("squarefeet vs price")
plt.xlabel("squarefeet")
plt.ylabel("price")
plt.grid(True)
plt.show()

# Step 3: Feature and Target Selection
X = df[['squarefeet']]   # Independent variable
y = df['price']              # Dependent variable

# Step 4: Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Model Building
model = LinearRegression()
model.fit(X_train, y_train)

# Regression parameters
print("\n===== Regression Coefficients =====")
print(f"Intercept (b₀): {model.intercept_}")
print(f"Coefficient (b₁): {model.coef_[0]}")

# Step 6: Prediction and Evaluation
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n===== Evaluation Metrics =====")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# Step 7: Visualization
# Plot regression line
plt.figure(figsize=(7, 5))
plt.scatter(X_test, y_test, color='blue', label='Actual Values')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title("Regression Line: squarefeet vs price")
plt.xlabel("squarefeet")
plt.ylabel("price")
plt.legend()
plt.show()

# Plot actual vs predicted
plt.figure(figsize=(6, 5))
sns.scatterplot(x=y_test, y=y_pred, color='green')
plt.title("Actual vs Predicted Prices")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.grid(True)
plt.show()
