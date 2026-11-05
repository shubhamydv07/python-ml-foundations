try:
    a = int(input("Enter the number whose table wants : "))
    Table = [i*a for i in range(1,11)]
    print(Table)

    with open("Tables.txt" , "+a") as f:
        f.write(f"Table of {a} is - {str(Table)} \n")

        
except ValueError:
    print("Invalid input")

