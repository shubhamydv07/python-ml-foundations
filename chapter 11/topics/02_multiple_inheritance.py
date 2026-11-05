class Employee:
    company = "google"
    salary = 1000000
    
    def show(self):
        print(f"the company is {self.company} and salary is {self.salary}")

class Coder:
    language = "Python"

    def printLnguages(self):
        print(f"out of all the languages here is your language : {self.language}")

class Programmer(Employee , Coder):
    company = "alphabets google"
    
    def showLanguage(self):
        print(f"the company is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLnguages()
b.showLanguage()


