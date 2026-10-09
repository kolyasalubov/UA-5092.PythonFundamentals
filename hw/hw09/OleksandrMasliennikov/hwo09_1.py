from random import randint

SECRET_NUMBER = randint(1, 100)
MAX_ATTEMPTS = 10

print("I'm thinking of a number from 1 to 100.")
print(f"You have {MAX_ATTEMPTS} attempts to guess it.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        guess = int(input(f"Attempt {attempt}: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess < SECRET_NUMBER:
        print("The hidden number is greater.")
    elif guess > SECRET_NUMBER:
        print("The hidden number is less.")
    else:
        print(f"Congratulations! You guessed the number in {attempt} attempts.")
        break
else:
    print(f"You lost. The hidden number was {SECRET_NUMBER}.")
