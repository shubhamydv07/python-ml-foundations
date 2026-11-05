class Number:
    def __init__(self , n):
        self.n = n

    def __add__(self , num): # this is used for sum 
        return self.n + num.n # self.n will append 1st number and num.n will append second number

    def __mul__(self , num): # this is used for multiplication
        return self.n * num.n
    
    def __truediv__(self , num): # this is used for division
        return self.n / num.n
    
    def __floordiv__(self , num): # this is used for floor division
        return self.n // num.n
    
    def __sub__(self , num): # this is used for subtraction
        return self.n - num.n
    
    def __len__(self): # used to set what gets displayed upon calling.__len__() or len(obj)
        return 1
    
    def __str__(self): # used to set what gets displayed upon calling str(obj)
        return f"the number is {self.n}"





n = Number(1)
m = Number(2)

print(n+m)
print(n*m)
print(n/m)
print(n//m)
print(n-m)
print(len(n))
print(n)
