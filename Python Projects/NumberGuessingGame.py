import random

def number_guessing_game():
    print("Welcome to the Harder Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it correctly!")

    # Computer picks a random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            # Asking the user for his guess
            guess = int(input("Attempt " + str(attempts + 1) + "/" + str(max_attempts) + " - Make a guess: "))
            attempts += 1

            # Checking if the guess is correct or not
            if guess < number_to_guess:
                print("Too low! Try again.")
                print("Range: " + str(guess) + " to 100")
            elif guess > number_to_guess:
                print("Too high! Try again.")
                print("Range: 1 to " + str(guess))
            else:
                print("Congrats! You've guessed the correct number " + str(number_to_guess) + " in " + str(attempts) + " attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    else:
        # If the user runs out of attempts, retrun with the correct answer and better luck next time!
        print("Sorry! You've run out of attempts. The correct number was " + str(number_to_guess) + ". Better Luck Next time!")

# Running the game
number_guessing_game()
