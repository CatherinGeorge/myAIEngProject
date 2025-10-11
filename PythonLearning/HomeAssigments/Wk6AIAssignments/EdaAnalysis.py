# covid_eda_analysis.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class CovidEDA:
    def __init__(self, filename):
        # 1️⃣ Load dataset and keep only relevant columns
        self.df = pd.read_csv(
        r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\HomeAssigments\Wk6AIAssignments\country_wise_latest.csv"
    )
        if "New cases" in self.df.columns:
            self.df = self.df[["Confirmed", "New cases"]].copy()
        else:
            raise KeyError("Column 'New cases' not found in dataset!")
        print("✅ Dataset Loaded Successfully!")
        print(self.df.head(), "\n")

    # 2️⃣ Statistical Measures
    def compute_statistics(self):
        print("📊 Statistical Measures:")
        mean_vals = self.df.mean()
        median_vals = self.df.median()
        variance_vals = self.df.var()
        std_vals = self.df.std()
        corr_matrix = self.df.corr()

        print(f"Mean:\n{mean_vals}\n")
        print(f"Median:\n{median_vals}\n")
        print(f"Variance:\n{variance_vals}\n")
        print(f"Standard Deviation:\n{std_vals}\n")
        print(f"Correlation Matrix:\n{corr_matrix}\n")

    # 3️⃣ Outlier Detection & Removal using IQR
    def remove_outliers(self):
        print("🚫 Detecting and Removing Outliers using IQR Method...\n")
        Q1 = self.df.quantile(0.25)
        Q3 = self.df.quantile(0.75)
        IQR = Q3 - Q1

        # Filter non-outlier rows
        cleaned_df = self.df[~(
            (self.df < (Q1 - 1.5 * IQR)) |
            (self.df > (Q3 + 1.5 * IQR))
        ).any(axis=1)]

        print(f"Before Cleaning: {self.df.shape[0]} rows")
        print(f"After Cleaning: {cleaned_df.shape[0]} rows\n")

        self.cleaned_df = cleaned_df
        print("Cleaned Data Sample:")
        print(cleaned_df.head(), "\n")

    # 4️⃣ Normalization using StandardScaler
    def normalize_data(self):
        print("⚙️ Applying StandardScaler Normalization...\n")
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(self.cleaned_df)

        scaled_df = pd.DataFrame(
            scaled_data,
            columns=self.cleaned_df.columns
        )
        self.scaled_df = scaled_df

        print("Normalized (Scaled) Data Sample:")
        print(scaled_df.head(), "\n")

    # 5️⃣ Visualization using Seaborn
    def visualize(self):
        print("📈 Generating Visualizations...\n")

        # Histogram before normalization
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        sns.histplot(self.df["Confirmed"], kde=True, color='skyblue')
        plt.title("Confirmed Cases (Before Normalization)")

        plt.subplot(1, 2, 2)
        sns.histplot(self.df["New cases"], kde=True, color='orange')
        plt.title("New Cases (Before Normalization)")
        plt.tight_layout()
        plt.show()

        # Histogram after normalization
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        sns.histplot(self.scaled_df["Confirmed"], kde=True, color='green')
        plt.title("Confirmed Cases (After Normalization)")

        plt.subplot(1, 2, 2)
        sns.histplot(self.scaled_df["New cases"], kde=True, color='red')
        plt.title("New Cases (After Normalization)")
        plt.tight_layout()
        plt.show()

        # Heatmap for correlation
        plt.figure(figsize=(6, 4))
        sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap (Before Cleaning)")
        plt.show()


# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":
    # Replace the path with your CSV file path if needed
    covid_eda = CovidEDA("country_wise_latest.csv")

    covid_eda.compute_statistics()
    covid_eda.remove_outliers()
    covid_eda.normalize_data()
    covid_eda.visualize()
