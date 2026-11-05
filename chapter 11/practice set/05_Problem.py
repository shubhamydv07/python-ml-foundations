class Vector:
    def __init__(self , i , j , k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"Vector ({self.i} , {self.j} , {self.k})"

    def __add__(self , v):
        return Vector(self.i + v.i , self.j + v.j , self.k + v.k)
    
    def __mul__(self , v):
        result = self.i * v.i + self.j * v.j + self.k * v.k
        return result
    

a = Vector(2 , 4 , -6)
b = Vector(1 , 2 , 3)

print(a+b)
print(a*b)
