import random

computer = random.choice([1, -1, 0])

yourchoice = input("Enter your choice (s/w/g): ")

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "snake",
    -1: "water",
    0: "gun"
}

if yourchoice not in youDict:
    print("Invalid input")
    exit()

you = youDict[yourchoice]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")

elif (
    (computer == 1 and you == -1) or
    (computer == -1 and you == 0) or
    (computer == 0 and you == 1)
):
    print("Computer wins")

else:
    print("You win")