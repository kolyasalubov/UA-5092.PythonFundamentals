import random


attempts = 10
number = random.randint(1, 100)

while attempts > 0:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if not 1 <= guess <= 100:
        print("Please enter a number between 1 and 100.")
        continue
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempts -= 1
else:
    print("Sorry, you've run out of attempts. The number was", number)
