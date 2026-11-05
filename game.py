import keyboard
import random
import os
import time

WIDTH = 30
HEIGHT = 15

snake = [(7 , 10) , (7 , 9) , (7 , 8)]
direction = "right"
food = (random.randint(1 , HEIGHT - 2), random.randint(1 , WIDTH - 2))
score = 0
speed = 0.15

def clear():
    os.system("cls")

    def draw():
        clear()
        for y in range(HEIGHT):
             for x in range(WIDTH):
                 if (y , x) == snake[0]:
                     print("0", end="")
                 elif (y,x) in snake:
                     print("0", end="")
                 elif (y , x) == food:
                     print("X", end="")
                 elif y == 0 or y== HEIGHT-1 or x==0 or x == WIDTH-1:
                     print("#" , end="")
                 else:
                     print("", end="")
        print()
    print("Score:", score)

while True:
                    if keyboard.is_pressed("w") and direction != "DOWN" :
                        direrction = "UP"
                    elif keyboard.is_pressed("s") and direction != "UP" :
                        direction = "DOWN"
                    elif keyboard.is_pressed("a") and direction != "RIGHT" :
                        direction = "LEFT"
                    elif keyboard.is_pressed("d") and direction != "LEFT" :
                        direction = "RIGHT"

                        head_y,head_x = snake[0]
                        if direction == "UP":
                            new_head = (head_y-1 , head_x)
                        elif direction == "DOWN" :
                            new_head = (head_y+1 , head_x)
                        elif direction == "LEFT":
                            new_head = (head_y , head_x-1)
                        else :
                            new_head = (head_y , head_x+1)

                            if (new_head in snake or 
                                new_head[0] in [0 , HEIGHT -1] or
                                new_head[1] in [0 , WIDTH-1]):
                                clear()
                                print("GAME OVER")
                                print("Final Score:",score)
                                break

                            snake.insert(0 , new_head)

                            if new_head == food:
                                score +=1
                                speed *= 0.95 #speed increases
                                food = (random.randint(1 , WIDTH-2))
                            else:
                                snake.pop()
                                

                            
                            
                            





