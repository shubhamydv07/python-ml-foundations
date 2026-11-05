f = open("myfiles.txt" , "r")

read = f.read()
print(read)

f.close()
# the same can be written using the statement like this
with open("myfiles.txt") as f:
    print(f.read())

# you don't have to explicitily close the file