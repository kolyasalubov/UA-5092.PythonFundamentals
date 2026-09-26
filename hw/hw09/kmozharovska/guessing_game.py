from random import randint

"""
Game script that randomly generates a number from a range of
1 to 100 and asks the user to guess that number in 10 tries.
"""


def guess_number() -> None:
    """
    Function asks the user to guess the number
    and prompts whether the guess was correct.
    Args: None
    Returns: None
    """
    number = randint(1, 100)
    attempts = 10

    print("I have chosen a number from 1 to 100.")
    print("You have 10 attempts to guess it!")

    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt}/10.")
        guess = int(input("Please, enter your guess: "))

        if guess == number:
            print(f"Congratulations! You guessed the number {number}!")
            break
        elif guess < number:
            print("The number is greater than your guess.")
        else:
            print("The number is less than your guess.")
    else:
        print("Sorry, you've used all 10 attempts.")


if __name__ == "__main__":
    guess_number()
