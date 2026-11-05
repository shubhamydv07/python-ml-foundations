def sum(n):
    if n== 1:
        return 1
    return n + sum(n-1)

n = int(input("Enter any number :"))

if n<=0:
    print("Invalid input! Please enter a positive integer.")

else:
    print(f"the sum of first {n} natural numbers are {sum(n)}")