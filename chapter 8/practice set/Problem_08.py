#  USING RECURSION
def table(n, i=1):
    """Prints the multiplication table of a number using recursion."""
    if i > 10:
        return
    print(f"{n} X {i} = {n * i}")
    table(n, i + 1)

n = int(input("Enter any number: "))

print(f"Multiplication table of {n}:")
table(n)


# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n * i}")

# n = int(input("Enter the number whose table you want :"))
# table(n)