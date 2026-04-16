def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def read_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    n = read_non_negative_integer("Enter a number: ")
    print(f"Factorial of {n}: {factorial(n)}")
    print(f"Fibonacci of {n}: {fibonacci(n)}")