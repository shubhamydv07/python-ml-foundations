# try:
#     with open("file_2nd_question.txt") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error ! File not found")

with open("file_2nd_question.txt") as f:
    content = f.readlines()
    for line in content:
        print(line, end = "")
