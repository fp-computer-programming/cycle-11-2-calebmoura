# Author: Caleb Moura

# Removing spaces & converting to lowercase, then checking if string is equal to its reverse.
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Testin string function and printing palindrome.
if __name__ == "__main__":
    test_strings = ["racecar", "rotor", "hello"]
    for test_string in test_strings:
        print(f"'{test_string}' is a palindrome:", is_palindrome(test_string))