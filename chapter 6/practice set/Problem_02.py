a = int(input("Enter marks of 1st subject out of 100 :"))
b = int(input("Enter marks of 2st subject out of 100 :"))
c = int(input("Enter marks of 3st subject out of 100 :"))

d = (a + b + c)/3

if(a<0 or a>100 or b<0 or b >100 or c<0 or c>100):
    print("Please enter valid number out of 100")

elif (d>=40 and a>=33 and b>=33 and c>=33):
    print("You are passed ,total percentage is",d)

else:
    print("You are Failed , Try again next year!")