from random import randint

def guess_number():
    """Let the user guess a random number in 10 attempts."""
    secret_number = randint(1, 100)
    max_attempts = 10
    print("Guess the number between 1 and 100!")
    print("You have 10 attempts.")
    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f"\nAttempt {attempt}/10: "))
                if 1 <= guess <= 100:
                    break
                print("Enter a number between 1 and 100.")
            except ValueError:
                print("Please enter a valid number.")
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempt} attempts!")
            return
        elif guess < secret_number:
            print("The secret number is higher!")
        else:
            print("The secret number is lower!")
    print(f"\nGame over! The number was {secret_number}.")

if __name__ == "__main__":
    guess_number()