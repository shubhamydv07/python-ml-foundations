def is_even(n):
    if n % 2==0:
        print(f"{n} is even")
        return True
    else:
        print(f"{n} is odd")
        return False
    
n = int(input("Enter any number :"))
print(is_even(n))
