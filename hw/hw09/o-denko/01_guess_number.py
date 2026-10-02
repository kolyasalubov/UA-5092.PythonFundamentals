import random


def play_game(max_attempts: int = 10, min_num: int = 1, max_num: int = 100) -> None:
    """
    Plays a number guessing game within a specified range and attempt limit.
    Args:
        max_attempts: The maximum number of attempts allowed. Defaults to 10.
        min_num: The lower bound of the random number range. Defaults to 1.
        max_num: The upper bound of the random number range. Defaults to 100.
    """
    secret_number = random.randint(min_num, max_num)

    for count in range(1, max_attempts + 1):
        guess_number = get_user_guess(min_num, max_num)

        if guess_number == secret_number:
            print(f"You guessed it! Attempts used: {count}")
            break
        elif guess_number < secret_number:
            print("The secret number is greater than your guess")
        else:
            print("The secret number is less than your guess")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The secret number was: {secret_number}")


def get_user_guess(min_num: int, max_num: int) -> int:
    """
    Asks the user for input until a valid integer is entered.
    """
    while True:
        try:
            return int(input(f"Enter a number between {min_num} and {max_num}: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    play_game()
