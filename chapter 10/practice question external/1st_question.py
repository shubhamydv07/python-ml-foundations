class Person:

    def __init__(self , name , age):
        self.name = name
        self.age = age
        

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")


a = Person("Shubham Yadav" , 18)
a.greet()

