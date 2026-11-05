
import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([1,-1,0])

yourchoice = input("Enter your choice :")

youDict = {"s" : 1 , "w" : -1 , "g" : 0}

if yourchoice not in youDict:
    print("Invalid input")
    exit()

reverseDict = {1 : "snake" , -1 : "water" , 0 : "gun"}

you = youDict[yourchoice]

# By now we have 2 numbers(variabes) , you and computer 

print(f"You choose {reverseDict[you]} \ncomputer choose {reverseDict[computer]}")

if (computer == you):
    print("It's draw ")

else:
        if (computer - you == -1) or (computer - you == 2):
            print("Computer wins")
        
        else:
            print("You wins") 