class Employee:
    a = 1

    @classmethod # used for access class attributes
    def show(cls): # for class method cls will be used
        print(f"the class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self , value):
        self.fname = value.split()[0]
        self.lname = value.split()[1]


e = Employee()

e.a = 45

e.name = "shubham yadav"
print(e.fname , e.lname)
e.show()
