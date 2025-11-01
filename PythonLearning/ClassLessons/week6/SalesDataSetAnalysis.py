# sales_dataset_analysis.py
import pandas as pd

# Load Dataset
# Auto-detect the dataset file
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "SalesDataSet.csv")

# df = pd.read_csv(file_path)

df = pd.read_csv(r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\ClassLessons\week6\SalesDataSet.csv")
print("Dataset Loaded Successfully!")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("-" * 50)

# Compute Percentiles for Total Amount
p25 = df["Total Amount"].quantile(0.25)
p50 = df["Total Amount"].quantile(0.50)  # median
p75 = df["Total Amount"].quantile(0.75)

print("1. 25th Percentile of Total Amount:", round(p25, 2))
print("2. Median (50th Percentile) of Total Amount:", round(p50, 2))
print("3. 75th Percentile of Total Amount:", round(p75, 2))
print("-" * 50)

# Variance Calculations
var_total = df["Total Amount"].var()
var_qty = df["Quantity"].var()

print("4. Variance in Total Amount:", round(var_total, 2))
print("5. Variance in Quantity Sold:", round(var_qty, 2))
print("-" * 50)

# Correlation Analysis
corr_age_total = df["Age"].corr(df["Total Amount"])
corr_qty_total = df["Quantity"].corr(df["Total Amount"])
corr_price_total = df["Price per Unit"].corr(df["Total Amount"])

print("6. Correlation between Age and Total Amount:", round(corr_age_total, 3))
print("7. Correlation between Quantity and Total Amount:", round(corr_qty_total, 3))
print("8. Correlation between Price per Unit and Total Amount:", round(corr_price_total, 3))
print("-" * 50)

print("Analysis Completed Successfully!")
