import random

def game():
    return random.randint(1, 100)

new_score = game()
print(new_score)

with open("Hi-score.txt", "a+") as file:

    file.seek(0)   # move cursor to beginning
    content = file.read()

    if content == "":
        file.write(str(new_score))

    else:
        old_score = int(content)

        if new_score > old_score:
            file.seek(0)  # it will movee cursor to starting to replace words/numbers
            file.truncate() # it will remove extra which left after replacing
            file.write(str(new_score))













