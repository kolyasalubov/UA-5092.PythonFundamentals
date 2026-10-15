from random import randint

def play_guessing_game():
    """
    The function generates a random integer in the range from 1 to 100.
    The user is given 10 attempts to guess this number. 
    """

    secret_number = randint(1, 100)
    attempts_left = 10

    print("I have chosen a number between 1 and 100. You have 10 attempts to guess it!")

    while attempts_left > 0:
        guess_str = input(f"\nAttempts left: {attempts_left}. Enter your number: ")

        if not guess_str.isdigit():
            print("Please enter a valid integer.")
            continue
            
        guess = int(guess_str)
        attempts_left -= 1 

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}!")
            return  
        elif secret_number > guess:
            print("My number is GREATER than yours.")
        else:
            print("My number is LESS than yours.")

    print(f"\nUnfortunately, you have run out of attempts. My number was {secret_number}.")

if __name__ == "__main__":
    play_guessing_game()