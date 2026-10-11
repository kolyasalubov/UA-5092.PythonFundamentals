from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10


def get_guess() -> int:
    """
    Ask the user for a guess until a valid integer in range is entered.

    Non-numeric input and numbers outside the allowed range are rejected with a message, and the user is asked again.
    """
    while True:
        try:
            guess = int(input(f"Enter your guess ({MIN_NUMBER}-{MAX_NUMBER}): "))
        except ValueError:
            print("That's not a number. Please enter an integer.")
            continue

        if MIN_NUMBER <= guess <= MAX_NUMBER:
            return guess
        print(f"The number must be between {MIN_NUMBER} and {MAX_NUMBER}.")


def guess_the_number() -> None:
    """
    Play a number guessing game.

    The computer picks a random number from 1 to 100, and the user has 10 attempts to guess it. After each wrong guess, the program says whether the secret number is greater or less. Invalid input does not count as an attempt.
    """
    secret_number = randint(MIN_NUMBER, MAX_NUMBER)
    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = get_guess()

        if guess < secret_number:
            print("The secret number is greater than your guess.")
        elif guess > secret_number:
            print("The secret number is less than your guess.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempt(s)!")
            return
        if attempt < MAX_ATTEMPTS:
            print(f"Attempts left: {MAX_ATTEMPTS - attempt}")
    print(f"Game over! You didn't make it in {MAX_ATTEMPTS} attempts. The number was {secret_number}.")


if __name__ == "__main__":
    guess_the_number()
