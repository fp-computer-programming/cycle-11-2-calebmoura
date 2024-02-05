# Author: Caleb Moura

# Starting Fibonacci sequence with 0 and 1, generating fibonacci numbers, then returning the sum.
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    print("Fibonacci Sequence:", fib_seq)
    return sum(fib_seq)

# Fibonacci sequence result print,and sum of nubers also print.
def main():
    user_input = int(input("Enter a number between 2 and 100: "))
    if 2 <= user_input <= 100:
        total_sum = fibonacci(user_input)
        print("Sum of Fibonacci sequence:", total_sum)
    else:
        print("Invalid input. Please enter a number between 2 and 100.")

if __name__ == "__main__":
    main()