f = open("file.txt")

read = f.readlines() # it will read all lines
print(read , type(read))
f.close()


# it will read lines one by one from top to bottom
# lines1 = f.readline()
# print(lines1)
# lines1 = f.readline()
# print(lines1)