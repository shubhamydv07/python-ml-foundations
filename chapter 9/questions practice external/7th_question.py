with open("Questions.txt") as f:
    content = f.read()

with open ("Questions_copy.txt" , "w") as f:
    f.write(content)