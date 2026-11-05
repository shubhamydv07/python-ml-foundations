with open("main.py" , "r") as f:
    content1 = f.read()

with open("main_copy.py" , "r") as f:
    content2 = f.read()

if content1 == content2:
    print ("same")

else:
    print("not same")
