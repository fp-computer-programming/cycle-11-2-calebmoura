# Author: Caleb Moura

# Set list of numbers.
numbers = [3, 6, 7, 12, 15, 17, 21, 23, 27, 30]

# Iterate through the list provided, and check if number is or is not a multiple of 3. If not: skip, if is: print.
for num in numbers:
    if num % 3 != 0:
        continue
    print(num)