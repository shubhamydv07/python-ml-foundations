word = input("Enter the word you want to search :").lower()

with open("Questions.txt") as f:
    words = f.read().lower().split()
    if word in words:
        print("Word found")
    else:
        print("Word not found")
