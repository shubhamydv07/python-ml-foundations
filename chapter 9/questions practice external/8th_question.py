try:
    with open("Questions.txt") as f:
        content = f.read()

    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")

    replaced = content.replace(old_word, new_word)

    with open("Questions.txt", "w") as f:
        f.write(replaced)

    print(f"'{old_word}' replaced with '{new_word}' successfully!")

except FileNotFoundError:
    print("Error! File not found.")