# Author: Caleb Moura

# Importing random.
import random

# Defining the number guess & setting the target value to 1-100 from random import, then setting the trigger to higher or lower hints.
def number_guess():
    target_number = random.randint(1, 100)
    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess == target_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < target_number:
            print("Incorrect. # is higher than your guess.")
        else:
            print("Incorrect. # is lower than your guess.")

if __name__ == "__main__":
    number_guess()