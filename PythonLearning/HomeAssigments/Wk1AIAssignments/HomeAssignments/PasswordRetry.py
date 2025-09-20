# Password Retry System

# Step 1: Store the correct password
correct_password = "openAI123"

# Step 2: Allow the user 3 attempts
for attempt in range(1, 4):   # loop runs 3 times
    entered_password = input("Enter password: ")
    
    # Step 3: Check if the entered password is correct
    if entered_password == correct_password:
        print("Login Successful")
        break   # stop loop immediately if correct
    else:
        print(f"Incorrect password. Attempt {attempt} of 3.")
else:
    # Step 4: If all 3 attempts fail
    print("Account Locked")
