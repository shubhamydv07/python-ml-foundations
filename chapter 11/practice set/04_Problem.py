class Complex:
    def __init__(self , r , i):
        self.real = r
        self.imaginary = i

    def __add__(self , c):
        return Complex(self.real + c.real , self.imaginary + c.imaginary)
    
    def __mul__(self , c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal , mulImg)
    
    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"
    
a = Complex(1 , 2)
b = Complex(3 , 4)

print(a+b)
print(a*b)