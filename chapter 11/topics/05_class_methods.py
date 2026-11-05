class Employee:
    a = 1

    @classmethod # used for access class attributes
    def show(cls): # for class method cls will be used
        print(f"the class value of a is {cls.a}")

e = Employee()

e.a = 45
e.show()
