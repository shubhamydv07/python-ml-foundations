a = int(input("Enter your marks out of 100:"))

if (a>=90 and a<=100):
    print("You got 'Ex' grade")

elif(a >=80 and a<90):
    print("You got 'A' grade")

elif(a >=70 and a<80):
    print("You got 'B' grade")

elif(a >=60 and a<70):
    print("You got 'C' grade")

elif(a >=50 and a<60):
    print("You got 'D' grade")

elif(a >=0 and a<50):
    print("You got 'F' grade")

else:
    print("Invalid marks")