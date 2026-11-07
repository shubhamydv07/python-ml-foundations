# It formats the values inside the string into a desired output

# Sample = Template.format(p1,p2,p3.....)

# def format(a,b):
#     print("{} is a good {}".format(a, b))

# format("Shubham","boy")

a = "{} is a good {}".format("Shubham", "boy")
print(a)

# Can also choose the position of arguments using number start from 0
a = "{1} is a good {0}".format("Shubham", "boy")
print(a)