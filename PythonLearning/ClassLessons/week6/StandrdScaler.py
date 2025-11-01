# standard_scaler_example.py
from sklearn.preprocessing import StandardScaler

# Step 1️: Create the data
data = [[1, 2], [3, 4], [5, 6]]

# Step 2️: Create a StandardScaler object
scaler = StandardScaler()

# Step 3️: Fit the scaler to the data (compute mean and std dev)
scaler.fit(data)

# Step 4️: Transform the data
scaled_data = scaler.transform(data)

# Step 5️: Print the results
print("Original Data:\n", data)
print("\nMean:", scaler.mean_)
print("Standard Deviation:", scaler.scale_)
print("\nScaled Data:\n", scaled_data)
