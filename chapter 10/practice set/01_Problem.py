class Programmer:
    company = "Microsoft"
    def __init__(self , name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin


P = Programmer("Shubham Yadav" , 1500000 , 123001)
print(P.name , P.salary , P.pin , P.company)
Rohan = Programmer("Rohan Yadav" , 1500000 , 123001)
print(Rohan.name , Rohan.salary , Rohan.pin , Rohan.company)