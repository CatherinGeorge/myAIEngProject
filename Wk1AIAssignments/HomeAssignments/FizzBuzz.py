# Define the fizzbuzz function
def fizzbuzz(n):
    for i in range(1, n + 1):   # loop from 1 to n
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")   # divisible by both 3 and 5
        elif i % 3 == 0:
            print("Fizz")       # divisible only by 3
        elif i % 5 == 0:
            print("Buzz")       # divisible only by 5
        else:
            print(str(i))       # not divisible by 3 or 5

# Get user input
try:
    n = int(input("Enter a positive integer: "))
    if n > 0:
        fizzbuzz(n)  # call function
    else:
        print("Please enter a positive integer greater than 0.")
except ValueError:
    print("Invalid input! Please enter an integer.")
