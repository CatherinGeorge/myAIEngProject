# pandas_missing_data.py
import pandas as pd
import numpy as np

# Step 1️⃣: Create the CSV file (only needed once)
data = [
    ["TestCase", "Module", "Status", "Duration", "Defects"],
    ["TC1", "Login", "Passed", 12, 0],
    ["TC2", "Login", "Failed", np.nan, 2],
    ["TC3", "Payment", "Passed", 20, np.nan],
    ["TC4", "Payment", "Failed", 18, 3],
    ["TC5", "Reports", np.nan, 25, 0]
]

# Convert to DataFrame (ignore first row of column names since we'll set them manually)
columns = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=columns)

# Save to CSV (simulating the provided dataset)
df.to_csv("test_results_missing.csv", index=False)
print("✅ CSV file 'test_results_missing.csv' created successfully.\n")

# Step 2️⃣: Read the dataset
df = pd.read_csv("test_results_missing.csv")
print("Original DataFrame:")
print(df)
print("-" * 60)

# Step 3️⃣: Detect Missing Values
print("🔍 Missing Values per Column:")
print(df.isnull().sum())
print("-" * 60)

# Step 4️⃣: Handle Missing Values
# Replace missing Duration with mean
mean_duration = df["Duration"].mean()
df["Duration"].fillna(mean_duration, inplace=True)

# Replace missing Status with "Unknown"
df["Status"].fillna("Unknown", inplace=True)

print("After Filling Missing Values:")
print(df)
print("-" * 60)

# Step 5️⃣: Drop any remaining rows with missing data
df.dropna(inplace=True)

print("✅ Cleaned DataFrame (after dropping remaining NaNs):")
print(df)
print("-" * 60)

# Optional: Save cleaned data for reference
df.to_csv("test_results_cleaned.csv", index=False)
print("💾 Cleaned data saved to 'test_results_cleaned.csv'")
