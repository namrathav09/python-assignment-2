import random

def number_guessing_game():

    while True:
        print("\n----- Number Guessing Game -----")
        print("Computer has selected a number between 1 and 100.")
        print("You have 7 chances to guess the number.")

        number = random.randint(1, 100)
        total_attempts = 7
        attempts_left = total_attempts
        guessed_correctly = False

        while attempts_left > 0:

            try:
                guess = int(input("Enter your guess: "))
            except:
                print("Please enter a valid number.")
                continue

            if guess == number:
                guessed_correctly = True
                attempts_used = total_attempts - attempts_left + 1
                print("Congratulations! You guessed the correct number.")
                print("You used", attempts_used, "attempt(s).")
                break

            elif guess > number:
                attempts_left = attempts_left - 1
                print("Your guess is too high.")
                print("Attempts remaining:", attempts_left)

            else:
                attempts_left = attempts_left - 1
                print("Your guess is too low.")
                print("Attempts remaining:", attempts_left)

        if guessed_correctly == False:
            print("You could not guess the number.")
            print("The correct number was:", number)

        choice = input("Do you want to play again? (yes/no): ")

        if choice.lower() != "yes":
            print("Game has been ended. Thank you for playing.")
            break


number_guessing_game()