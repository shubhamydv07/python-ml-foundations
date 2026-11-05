class Employee:
    company = "google"
    
    def show(self):
        print(f"the name is {self.name} and salary is {self.salary}")

# class Programmer:
#     company = "alphabets google"
#     def show(self):
#         print(f"the name is {self.name} and salary is {self.salary}")

#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
    company = "alphabets google"
    
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()
print(a.company)
print(b.company)


