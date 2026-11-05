class Employee:
    
    course = "Btech"
    college = "NIT KURUKSHETRA" # This is an class attribute
    salary = 1200000

    def getInfo(self): # we can take anyone , but generally we takes self , self is convention
        print(f"The course is {self.course}\nThe college is {self.college}")
    
    @staticmethod  # it is static method and used when we donot want to pass the object to an function
    def greet():
        print("Hello , How are you ?")



shubham = Employee() # This is an object / instance  attribute
shubham.college = "IIT DELHI"
print(shubham.course , shubham.college)
shubham.getInfo() #Employee.getInfo(shubham)

shubham.greet()
