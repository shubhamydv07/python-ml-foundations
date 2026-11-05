class Calculator:
    def __init__(self,n):
        self.n = n

    def Square(self):
        return self.n**2
    
    def Cube(self):
        return self.n**3
    
    def Squareroot(self):
        if self.n>=0:
            return self.n**0.5
        else:
            return "Invalid Input For square root"
while True:
    try:
        n = float(input("Enter any integer :"))
        break
    except ValueError:
        print("Invalid Input")

a = Calculator(n)
print(a.Square())
print(a.Cube())
print(a.Squareroot())