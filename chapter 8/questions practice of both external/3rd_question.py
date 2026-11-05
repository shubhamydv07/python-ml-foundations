def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c



a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))

print(f"the maximun number is {find_max(a,b,c)}")