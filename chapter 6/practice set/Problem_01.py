print("enter 4 numbers a, b , c , d :")
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
d = int(input("Enter d :"))

if (a>=b and a>=c and a>=d):
    print("a is the greatest number :" , a)

elif (b>=c and b>=d and b>=a):
    print("b is the greatest number :" , b)

elif (c>=d and c>=a and c>=b):
    print("c is the greatest number :" , c)

else :
    print("d is the greatest number :" , d)




# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# greatest = max(a, b, c, d)

# print("Greatest number is:", greatest)




# nums = [a, b, c, d]
# greatest = max(nums)

# count = nums.count(greatest)

# if count > 1:
#     print("Greatest number is:", greatest, "and it appears", count, "times")
# else:
#     print("Greatest number is:", greatest)