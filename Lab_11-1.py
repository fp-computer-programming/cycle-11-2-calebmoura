# Author: Caleb Moura

# Defining integers and adding them to the for loop.
def find_evens(num_A, num_B):
    evens = []
    for num in range(num_A, num_B):
        if num % 2 == 0:
            evens.append(num)
    return evens

# Setting variables equal to integers.
num_A = 4
num_B = 7

# Finding result and printing.
result = find_evens(num_A, num_B)
print(f"Even numbers from {num_A} to {num_B}: {result}")