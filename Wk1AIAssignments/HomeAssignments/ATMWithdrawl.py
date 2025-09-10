# ATM Withdrawal Simulation

# Step 1: Ask user for withdrawal amount
amount = int(input("Enter withdrawal amount: "))

# Step 2: Check if amount is valid (multiple of 100)
if amount % 100 == 0:
    # Step 3: Valid amount → Dispense money
    print(f"Dispensing {amount}")
else:
    # Step 4: Invalid amount
    print("Invalid amount")
