def countdown(n):
    if n < 0:       # base case — stop here
        return
    print(n)
    countdown(n - 1)  # recursive call

n = int(input("Enter any integer: "))

if n <= 0:
    print("Please enter a valid positive integer.")
else:
    countdown(n)