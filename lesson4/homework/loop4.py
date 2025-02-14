import random

while True:
    num = random.randint(1, 100)
    attempts = 10
    
    while attempts > 0:
        try:
            user = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if user > num:
            print("Too high!")
        elif user < num:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
        
        attempts -= 1
        print("Number of attempts you have:", attempts)
    
    if attempts == 0:
        print("You lost. Want to play again?")
    else:
        print("Want to play again?")
    
    cont = input("(Y/YES/y/yes/ok to continue): ").strip().lower()
    if cont not in ['y', 'yes', 'ok']:
        print("Thanks for playing!")
        break