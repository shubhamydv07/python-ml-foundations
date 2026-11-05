# a = int(input("enter first number : "))
# b = int(input("enter second number : "))

# if b == 0 :
#     raise ZeroDivisionError("Answer will be infinity , because division by zero is not allowed")

# else:
#     print(a/b)


try:
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))

    print(a/b)

except ZeroDivisionError:
    print("Infinity")



