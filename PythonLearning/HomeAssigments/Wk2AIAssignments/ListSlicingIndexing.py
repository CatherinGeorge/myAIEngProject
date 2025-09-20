# List of first ten prime numbers
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (a) Extract the middle five primes
middle_five = prime_numbers[3:8]

# (b) Get every second prime (starting from the first element)
every_second = prime_numbers[::2]

# (c) Use negative indexing to get last three primes
last_three = prime_numbers[-3:]

# (d) Reverse the list using slicing
reversed_list = prime_numbers[::-1]

# (e) Sort the list in descending order
descending_order = sorted(prime_numbers, reverse=True)

# Print results
print("Original List:", prime_numbers)
print("a) Middle Five Primes:", middle_five)
print("b) Every Second Prime:", every_second)
print("c) Last Three Primes:", last_three)
print("d) Reversed List:", reversed_list)
print("e) Descending Order:", descending_order)
