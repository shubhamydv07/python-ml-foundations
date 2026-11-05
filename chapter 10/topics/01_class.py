class Employee:
    course = "Btech"
    college = "NIT KURUKSHETRA" # This is an class attribute
    salary = 1200000

shubham = Employee() # This is an object / instance  attribute
shubham.name = "Shubham Yadav"
print(shubham.course , shubham.college , shubham.name)

rohan = Employee()
rohan.name = "Rohan Yadav Robinson"
print(rohan.salary , rohan.course , rohan.name)

# Here name is object/instance attribute and course , college ,
# salary are class attributes as they directly belong to the class 