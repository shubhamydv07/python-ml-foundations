def power(base,exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/power(base,-exp)
    return base * power(base,exp-1)

base = float(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

print(f"{base} to the power {exp} is {power(base,exp)}")