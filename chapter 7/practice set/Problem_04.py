# a = int(input("Enter any number :"))

# for i in range ( 2 , a):
#     if a % i ==0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")


a = int(input("Enter any number: "))

if a <= 1:
    print("Number is not prime")
else:
    for i in range(2, a):
        if a % i == 0:
            print("Number is not prime")
            break
    else:
         print("Number is prime")




