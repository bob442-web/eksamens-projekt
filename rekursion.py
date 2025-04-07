n = int(input("Enter a number to calculate its Fibonacci value: "))

def fibonacci(n):
    if n == 0:
        return 0  # basis-tilfælde / stop point
    elif n == 1:
        return 1  # basis-tilfælde / stop point
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # rekursivt kald

# Call the function and print the result
print(f"The Fibonacci value for {n} is {fibonacci(n)}")