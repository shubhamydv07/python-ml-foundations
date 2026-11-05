# Note: Instance attributes, take preference over class attributes
# during assignment & retrieval.

class Employee:
    
    course = "Btech"
    college = "NIT KURUKSHETRA" # This is an class attribute
    salary = 1200000

shubham = Employee() # This is an object / instance  attribute
shubham.college = "IIT DELHI"
print(shubham.course , shubham.college)
