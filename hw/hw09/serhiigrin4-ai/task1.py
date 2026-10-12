"""
HW09, Task 1. Guess the number game.

The program picks a random number from 1 to 100.
The user has 10 attempts to guess it. After each wrong attempt
the program says whether the secret number is greater or less
than the number entered by the user.
"""

from random import randint

secret_number = randint(1, 100)
max_attempts = 10

print("I have picked a number from 1 to 100. You have 10 attempts to guess it.")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts}. Your guess: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts!")
        break
    elif guess < secret_number:
        print("The secret number is greater than yours.")
    else:
        print("The secret number is less than yours.")
else:
    print(f"Game over! You have used all {max_attempts} attempts. The number was {secret_number}.")
