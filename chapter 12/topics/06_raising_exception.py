a = int(input("Enter first number:"))
b = int(input("Enter second number:"))


if (b==0):
    raise ZeroDivisionError("Hey you cannot divide by zero")

else:
    print(f"the division a/b is {a/b}")