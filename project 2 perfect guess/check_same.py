with open("main.py") as f:
    file1 = f.read()


with open("main_copy.py") as f:
    file2 = f.read()

if file1 == file2:
    print("same")
else:
    print("different")


