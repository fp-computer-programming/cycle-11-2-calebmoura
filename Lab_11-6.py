# Author: Caleb Moura

sum_of_numbers = 0

# Writing  program that prompts user to input a number using while loop.
while True:
    num = input("Enter a number (enter -1 to end): ")

# Check to see if number input is a valid number.
    try:
        num = float(num)
    except ValueError:
        print("Please enter a valid number.")
        continue

# If  user inputs a number, it is added to the sum of previously entered numbers, if "-1" is input by user the program ends.
    if num != -1:
        sum_of_numbers += num
    else:
        print("Sum of all numbers entered:", sum_of_numbers)
        break