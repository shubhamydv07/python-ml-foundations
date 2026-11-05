# Write a python program to print the contents of a directory
#  using the os module. Search online for the function which does that



import os
# specify the directory you want to list in below line after slash
directory_path = '/windows/system32' #write directory path after the first slash

# list all the files in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)