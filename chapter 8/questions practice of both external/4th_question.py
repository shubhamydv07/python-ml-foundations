def convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter the temperature in celsius: "))
print(f"the temperature in fahrenheit is {convert(celsius)}")