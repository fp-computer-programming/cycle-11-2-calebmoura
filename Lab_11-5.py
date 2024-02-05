# Author: Caleb Moura

# Function to print each name in the list same number of times as letters in name, then storing the names.
def name_multiplication():
    names = []

# Prompt user to input a name.
    for i in range(1):
        name = input("Enter a name: ")
        names.append(name)

# Printing each name in list same number of times as letters in the name.
    for name in names:

# For loop:
        for letter in name:
            print(name)

# While loop:
        count = 0
        while count < len(name):
            print(name)
            count += 1
        print()  

name_multiplication()