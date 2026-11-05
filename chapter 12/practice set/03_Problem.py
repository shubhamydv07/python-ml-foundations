try:
    a = int(input("Enter the number whose table wants : "))
    Table = [i*a for i in range(1,11)]
    print(Table)
except ValueError:
    print("Invalid input")

