def print_pattern(n):
    """Prints a decreasing pattern of stars using recursion."""
    if n <= 0:
        return
    print("*" * n)
    print_pattern(n - 1)

n = int(input("Enter any number: "))

if n <= 0:
    print("Invalid input! Please enter a positive integer.")
else:
    print_pattern(n)
