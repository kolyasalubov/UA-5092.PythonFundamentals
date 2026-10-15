from random import randint


MAX_TRIES = 10
HIGH = 100
LOW = 1


def guess_the_number() -> bool:
    """
    Play a number guessing game.

    The computer picks a random number from LOW to HIGH, and the user
    has MAX_TRIES attempts to guess it. After each wrong guess, the
    program says whether the secret number is greater or less.

    Returns True if the user guessed the number, otherwise False.
    """
    secret = randint(LOW, HIGH)
    print(f"I have picked a number from {LOW} to {HIGH}. "
          f"Try to guess the number, you have got {MAX_TRIES} tries.")

    for attempt in range(1, MAX_TRIES + 1):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if not LOW <= guess <= HIGH:
                    print(f"Please enter a number between {LOW} and {HIGH}.")
                    continue
                print(f"Attempt {attempt} and your guess is {guess}")
                break
            except ValueError:
                print("Please enter a whole number.")

        if guess == secret:
            print(f"Congratulations! You guessed the number {secret} in {attempt} attempt(s)!")
            return True
        elif guess < secret:
            print("The secret number is greater than your guess.")
        else:
            print("The secret number is less than your guess.")

    print(f"Sorry, you have used all your {MAX_TRIES} attempts and not guessed the number.\n"
          f"The number was {secret}")
    return False


if __name__ == "__main__":
    guess_the_number()