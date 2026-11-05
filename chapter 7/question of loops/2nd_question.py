# a = 0

# while(a>=0):
#     a = int(input("Enter any number :"))
#     print(a)

# print("You entered a negative number. Stopping.")

while True:
    a = int(input("Enter any number: "))
    if a < 0:
        break
    print(a)

print("You entered a negative number. Stopping.")