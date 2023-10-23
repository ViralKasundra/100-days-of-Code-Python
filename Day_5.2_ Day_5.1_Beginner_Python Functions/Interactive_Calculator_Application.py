import math
import time

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to calculate factorial recursively
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Lambda function to calculate square
square = lambda x: x**2

# Decorator function to log function calls
def log_function_call(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' called with arguments {args} returned {result}")
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
    return wrapper

# Generator function to generate Fibonacci numbers
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# User-friendly command-line interface
while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Factorial")
    print("6. Square")
    print("7. Fibonacci Generator")
    print("8. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '8':
        print("Goodbye!")
        break
    
    if choice not in ('1', '2', '3', '4', '5', '6', '7'):
        print("Invalid choice. Please select a valid option.")
        continue

    if choice in ('5', '6'):
        num = float(input("Enter a number: "))
    elif choice == '7':
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = factorial(int(num))
    elif choice == '6':
        result = square(num)
    elif choice == '7':
        for fib in fibonacci_generator(n):
            print(fib, end=" ")
        print("\n")
        continue
    
    print(f"Result: {result}")
