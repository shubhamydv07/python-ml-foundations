words = ["Donkey", "ganda", "bad"]

with open("file_problem_4.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file_problem_4.txt", "w") as f:
    f.write(content)