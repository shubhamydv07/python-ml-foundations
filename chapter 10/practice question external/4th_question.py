class Student:

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks>=90:
            return "'A' grade"
        elif self.marks>=80:
            return "'B' grade"
        elif self.marks>=70:
            return "'C' grade"
        elif self.marks>=60:
            return "'D' grade"
        else:
            return "'F' grade"


Name = input("Enter the name of student :")
while True:
    try:
        a = int(input("Enter the marks:"))
        if a<0 or a>100:
            raise ValueError
        else:
            Marks  = a
            break
    except ValueError:
        print("Enter valid marks between 0 - 100")
        continue
child = Student(Name , Marks)

print(child.grade())