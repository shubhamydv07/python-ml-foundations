class Employee:

    def __init__(self):
        print("constructor of Employee class")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__() # it will run the constructor of parent class "Employee" / calls constructor of base class
        print("constructor of Programmer class")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()  # It will run the constructor of the parent class "Programmer" / calls constructor of base class
        print("constructor of Manager class")
    c = 3

# o = Employee()

# print(o.a) 

# o = Programmer()

# print(o.a) 
# print(o.b) 

o = Manager()

print(o.a) 
print(o.b) 
print(o.c) 