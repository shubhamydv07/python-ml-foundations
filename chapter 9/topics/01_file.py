f = open('file.txt') # built in function in file to open a file
data = f.read() # to read the file
print(data)
f.close() # it is mandatory

# open function have default "r" read mode open("file.txt" , "r")