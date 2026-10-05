'''
This module implements a game in which the user must guess 
a number between 0 and 100 in 10 attempts.
'''
from random import randint

GOAL = randint(0, 100)
ATTEMPTS = 10

def guess_number() -> None:
    '''
    Function that asks the user for a number and prompts whether
    the number is greater or less than user`s number until
    user wins or runs out of attempts.
    Args: 
        None
    Returns: 
        None
    '''
    print("-" * 20 + "Guess the number" + "-" * 20)
    print("\nYou need to guess the number between 1 and 100.\n"
    f"You have {ATTEMPTS} attempts. Try it!\n"
    "Enter Q if you want to quit the game.")

    attempt = 1

    while attempt <= ATTEMPTS:

        user_input = input(f"{attempt} attempt -> Enter your number: ")

        if user_input.lower() == 'q':
            break

        try:
            user_input = int(user_input)
        except ValueError:
            print("It`s not a number!\n")
            continue

        if user_input < 0 or user_input > 100:
            print("Your number should be between 0 and 100.\n")
            continue

        if user_input == GOAL:
            print(f"You guessed right! It`s {user_input}. You did it in {attempt} attempts.")
            break
        elif user_input < GOAL:
            print(f"{user_input} is less than goal number. Try again!\n")
        else:
            print(f"{user_input} is greater than goal number. Try again!\n")

        attempt += 1
    else: 
        print("\nWhoops! You ran out of attempts:(\nMaybe next time!)")


if __name__ == "__main__":
    guess_number()