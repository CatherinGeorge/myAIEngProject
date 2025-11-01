# StudentPerformanceModel_Fixed.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder  # NEW IMPORT

class StudentPerformanceModel:
    def __init__(self, filepath):
        # Load dataset
        self.df = pd.read_csv(filepath)
        print("Dataset loaded successfully!\n")
        print("First 5 rows of data:")
        print(self.df.head())

    def preprocess(self):
        print("\n Checking for missing values:")
        print(self.df.isnull().sum())

        # Drop missing values
        self.df.dropna(inplace=True)
        print("\n Cleaned dataset shape:", self.df.shape)

        # Detect and encode categorical columns
        categorical_cols = self.df.select_dtypes(include=["object"]).columns.tolist()
        if categorical_cols:
            print("\n Encoding categorical columns:", categorical_cols)
            label_encoder = LabelEncoder()
            for col in categorical_cols:
                self.df[col] = label_encoder.fit_transform(self.df[col])
        else:
            print("\n No categorical columns found.")

        # Separate independent (X) and dependent (y) variables
        self.X = self.df.drop(columns=["Performance Index"])
        self.y = self.df["Performance Index"]

        print("\n Independent Features (X):", list(self.X.columns))
        print("Target Variable (y): Performance Index")

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        print("\n Data split into Train and Test sets:")
        print(f"Train Shape: {self.X_train.shape}, Test Shape: {self.X_test.shape}")

    def train_model(self):
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        print("\n Model Training Completed Successfully!")
        print(f"Intercept (β₀): {self.model.intercept_:.2f}")
        print(f"Coefficients (β): {self.model.coef_}")

    def evaluate_model(self):
        self.y_pred = self.model.predict(self.X_test)

        mse = mean_squared_error(self.y_test, self.y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, self.y_pred)

        print("\n Model Evaluation Results:")
        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
        print(f"R² Score: {r2:.2f}")

        # Scatter plot
        plt.figure(figsize=(7, 5))
        sns.scatterplot(x=self.y_test, y=self.y_pred, color='blue', s=80)
        plt.xlabel("Actual Performance Index")
        plt.ylabel("Predicted Performance Index")
        plt.title("Actual vs Predicted Student Performance")
        plt.grid(True)
        plt.show()

    def predict_user_input(self):
        print("\n Enter Student Details for Prediction:")
        user_values = []
        for feature in self.X.columns:
            val = float(input(f"Enter value for {feature}: "))
            user_values.append(val)

        user_array = np.array(user_values).reshape(1, -1)
        prediction = self.model.predict(user_array)[0]
        print(f"\n Predicted Student Performance Index: {prediction:.2f}")

    def visualize(self):
        plt.figure(figsize=(10, 5))
        sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap of Student Performance Data")
        plt.show()


# 9️ Main Execution
if __name__ == "__main__":
    file_path = r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\HomeAssigments\Wk8AIAssignments\Student_Performance.csv"

    model = StudentPerformanceModel(file_path)
    model.preprocess()
    model.split_data()
    model.train_model()
    model.evaluate_model()
    model.visualize()
    model.predict_user_input()

