try:

    with open ("1.txt","r") as f:
        print(f.read())

except FileNotFoundError:
    print("File 1.txt not found")

try:

    with open ("2.txt","r") as f:
        print(f.read())

except FileNotFoundError:
    print("File 2.txt not found")


try:

    with open ("3.txt","r") as f:
        print(f.read())

except FileNotFoundError:
    print("File 3.txt not found")

print("Thank you")