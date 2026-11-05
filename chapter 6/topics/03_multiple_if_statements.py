a = int(input("Enter your age  :"))

# If elif else ladder

# if statement numer : 1
if (a%2 == 0):    # This is independent if , no else or elif is in its loop , it will run independently
    print("a is even")
# end of if statement number : 1


# if statement numer : 
if (a>=18):
    print("You are above the age of consent")
    print("It is good for you")

elif (a==0):
    print("You entered 0 , which is invalid age")

elif (a<0):
    print("Error ! Please enter valid positive age")

else:
    print("You are below the age of consent")
# end of if statement number : 1

print("End of program")