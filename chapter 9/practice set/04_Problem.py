word = "Donkey"

with open("file_problem_4.txt" , "r") as f:
    content = f.read()

newcontent = content.replace("Donkey" , "######")

with open("file_problem_4.txt" , "w") as f:
    f.write(newcontent)