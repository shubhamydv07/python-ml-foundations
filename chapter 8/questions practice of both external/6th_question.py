def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers!"
    if (n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter any number: "))
print(f"the factorial of {n} is {factorial(n)}")