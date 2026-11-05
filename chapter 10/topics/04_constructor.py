class Employee:
    
    course = "Btech"
    college = "NIT KURUKSHETRA" 
    salary = 1200000

    def __init__(self , name , salary , college):  # dunder method , which is automatically called
        self.name = name  #in this self is appended to the object which we declared
        self.salary = salary # and self.salary is variable which we can use and salary after '=' is
        self.college = college # actaully our  defined salary like 1200000 etc. these are class assigned values
        print("I am creating an object")

    def getInfo(self):
        print(f"The course is {self.course}\nThe college is {self.college}")
    
    @staticmethod
    def greet():
        print("Hello , How are you ?")



shubham = Employee("Shubham Yadav" , 1300000 , "IIT DELHI")
shubham.name = "Shubham Yadav"
print(shubham.course , shubham.college , shubham.name ,shubham.salary)

# simran = Employee()