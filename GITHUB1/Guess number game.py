import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number=random.randint(1,100)
    attempts=0
    while True:
        try:
            guess=int(input("Enter your guess: "))
            attempts+=1
            if guess<1 or guess>100:
                print("Please guess a correct number.")
            elif guess<secret_number:
                print("Too low! try again.")
            elif guess>secret_number:
                print("Too high! Try again.")
            else:
                print(f" Congratulations! You guessed number{secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input.please enter a valid number.")
number_guessing_game()        
    
