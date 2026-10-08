from random import randint

def guess_the_number():
    """
    Play a number guessing game.

    The computer picks a random number from 1 to 100, and the user
    has 10 attempts to guess it. After each wrong guess, the program
    says whether the secret number is greater or less.
    """
    secret_number = randint(1, 100)
    attempts = 0
    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("The secret number is greater than your guess.")
        elif guess > secret_number:
            print("The secret number is less than your guess.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            return
    print(f"Game over! You didn't make it in 10 attempts :(")


if __name__ == "__main__":
    guess_the_number()