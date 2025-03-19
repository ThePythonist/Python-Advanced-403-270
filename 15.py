def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


n = int(input("Enter any number : "))

try:
    print(f"Factorial of {n} is {factorial(n)}")
except RecursionError:
    if n == 0:
        print("Factorial of 0 is 1")
    else:
        print("Only positive numbers have factorial")
