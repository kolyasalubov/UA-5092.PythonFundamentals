from random import randint

"""
Game script that randomly generates a number from a range of
1 to 100 and asks the user to guess that number in 10 tries.
"""
MIN_NUMBER = 1
MAX_NUMBER = 100
ATTEMPTS = 10


def guess_number() -> None:
    """
    Function asks the user to guess the number
    and prompts whether the guess was correct.
    Args: None
    Returns: None
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)

    print(f"I have chosen a number from {MIN_NUMBER} to {MAX_NUMBER}.")
    print(f"You have {ATTEMPTS} attempts to guess it!")

    for attempt in range(1, ATTEMPTS + 1):
        print(f"Attempt {attempt}/{ATTEMPTS}.")

        try:
            guess = int(input("Please, enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print("Out of bounds! Please stay between "
                  f"{MIN_NUMBER} and {MAX_NUMBER}.")
            continue

        if guess == number:
            print(f"Congratulations! You guessed the number {number}!")
            break
        elif guess < number:
            print("The number is greater than your guess.")
        else:
            print("The number is less than your guess.")
    else:
        print(f"Sorry, you've used all {ATTEMPTS} attempts.")


if __name__ == "__main__":
    guess_number()
