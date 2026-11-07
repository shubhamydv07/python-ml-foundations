def formatFunc():
    name = input("Enter your name : ")
    try:
        m = int(input("Enter your marks : "))
    except ValueError:
        print("Enter valid integer marks !")
    try:
        n = int(input("Enter your mobile number : "))
    except ValueError:
        print("Enter valid integer mobile number !")
    marks = str(m)
    mobile_number = str(n)

    a = "The name of the student is {}, his marks are {} and phone number is {}".format(name , marks , mobile_number)
    print(a)

formatFunc()





