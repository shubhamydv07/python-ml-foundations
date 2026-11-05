def inches_to_cm(inches):
    return inches * 2.54

inches = float(input("Enter the length in inches: "))

if inches < 0:
    print("Invalid input! Length cannot be negative.")
else:
    print(f"{inches} inches is equal to {inches_to_cm(inches)} centimeters.")