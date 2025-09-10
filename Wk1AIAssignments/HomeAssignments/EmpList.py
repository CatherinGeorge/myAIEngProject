# Employee List Program

# Step 1: Create a list of 5 employees (hardcoded)
employees = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Step 2: Use a loop with enumerate() to print names with numbers
for index, name in enumerate(employees, start=1):
    print(f"{index}. {name}")
