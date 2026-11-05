l = [ 2 ,53 ,18 ,67]

# index = 0
# for item in l:
#     print(f"the item number at index {index} is {item}")
#     index += 1

# This can be simplified using unumerate function
for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")