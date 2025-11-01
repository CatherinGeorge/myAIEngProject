# sales_outlier_analysis.py
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv(r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\ClassLessons\week6\SalesDataSet2.csv")

print("Dataset loaded successfully!")
print(f"Shape before cleaning: {df.shape}\n")

# Step 2️ Detect numeric columns only (IQR works for numeric data)
numeric_cols = df.select_dtypes(include=['number']).columns

# Step 3️ Compute IQR and detect outliers
outliers_df = pd.DataFrame()  # to store all outlier rows

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers for the current column
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

    if not outliers.empty:
        outliers_df = pd.concat([outliers_df, outliers])

# Remove duplicates if the same row was an outlier in multiple columns
outliers_df = outliers_df.drop_duplicates()

# Step 4️: Write outliers to CSV
outliers_df.to_csv("SalesDataset2_outliers.csv", index=False)
print(f" Outliers detected and saved to 'SalesDataset2_outliers.csv' ({outliers_df.shape[0]} rows).")

# Step 5️: Remove outliers from original data
cleaned_df = df[~df.index.isin(outliers_df.index)]

# Step 6️: Write cleaned data to new CSV
cleaned_df.to_csv("SalesDataset2_cleaned.csv", index=False)
print(f" Cleaned data saved to 'SalesDataset2_cleaned.csv' ({cleaned_df.shape[0]} rows).")

# Step 7️: Summary
print("\n--- Summary ---")
print("Original data:", df.shape)
print("Outliers found:", outliers_df.shape)
print("Cleaned data:", cleaned_df.shape)
