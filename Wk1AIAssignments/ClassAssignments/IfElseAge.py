age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))
print(f"Age: {age}, Experience: {experience}")

if age > 22 and experience >= 2:
    print("Access Granted")
else:
    print("Access Denied")