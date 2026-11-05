def fahrenheit(celsius):
     return (celsius * 9/5) + 32
     

celsius = float(input("Enter the temperature in celsius: "))
print(f"the temperature in fahrenheit is {fahrenheit(celsius)}")
