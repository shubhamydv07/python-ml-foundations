l = [1,2,3,4,5,6,7,8,9]

for index,item in enumerate(l):

    if index == 2 or index == 4 or index == 6:
        if index == 2:
            print(f"the {index + 1}rd element is {item}")
        else:
            print(f"the {index + 1}th element is {item}")

    else:
        continue