a = int(input("Enter your age  :"))

# If elif else ladder

if (a>=18):
    print("You are above the age of consent")
    print("It is good for you")

elif (a==0):
    print("You entered 0 , which is invalid age")

elif (a<0):
    print("Error ! Please enter valid positive age")

else:
    print("You are below the age of consent")

print("End of program")
