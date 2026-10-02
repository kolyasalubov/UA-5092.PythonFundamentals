from random import randint

def game_function():

    """
    Runs a number guessing game.

    The function generates a random integer between 1 and 100.
    The user has up to 10 attempts to guess the correct number,
    receiving hints ('HIGHER' or 'LOWER') after each valid guess.
    
    Returns:
        None
    """

    random_number = randint(1, 100)
    counter = 0

    print("Try to guess the number between 1 and 100 in 10 attempts!")

    while counter < 10:
        print(f"Round #{counter + 1}. Make your guess: ", end="")
        guess_value = int(input())

        if guess_value < 1 or guess_value > 100:
            print("Invalid input! Please enter a number between 1 and 100.")
            continue

        if guess_value < random_number:
            print(f"The number is HIGHER than {guess_value}.")
        elif guess_value > random_number:
            print(f"The number is LOWER than {guess_value}.")
        else:
            print(f"Congratulations! The number was {random_number}!")
            break
        counter += 1
    else:
        print("Game over! You didn't make it in 10 attempts :(")

if __name__ == "__main__":
    game_function()
