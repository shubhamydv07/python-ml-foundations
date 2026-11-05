import random

while True:
    while True:
        print('''Difficulties :-
              Easy : 1 - 10
              Medium : 1 - 50
              Hard : 1 - 100''')
    
        difficulty = input("Enter the difficulty level : ").lower()

        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            break
        else:
            print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

    if difficulty == "easy":
        end_range = 10
    elif difficulty == "medium":
        end_range = 50
    else:
        end_range = 100

    secret_number = random.randint(1 , end_range)

    print(f"Game Start! Guess a number between 1 and {end_range}")
    
    print(secret_number)
    
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Enter your number to guess: "))
            
        except ValueError:
            print(f"Enter valid integer between 1 and {end_range}")
            continue
    

        if user_guess < 1 or user_guess > end_range:
                print(f"Enter valid integer between 1 and {end_range}")
                continue
        
        else:
             attempts += 1
             if user_guess == secret_number:
                print(f"Congratulations! You guessed it right in {attempts} attempts!")
                break
    
             elif user_guess > secret_number:
                  print("Too high ! Try again")
    
             else:
                  print("Too low ! Try again")

    while True:
        play_again = input("Do you want to play again? (yes/no): " )
    
        if play_again.lower() != "yes" and play_again.lower() != "no":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        break

    if play_again.lower() == "yes":
        continue

    print("Thanks for playing!")
    break
              
        
    