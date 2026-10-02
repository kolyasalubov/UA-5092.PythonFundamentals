from random import randint



def guess_num() -> None:
    """
    Runs a number guessing game.

    The program generates a random number from 1 to 100.
    The user has 10 attempts to guess the number.

    Returns None.
    """
    number = randint(1, 100)

    for i in range(1, 11):
        print(f"Try number {i}")
        choice = int(input("Write number: "))

        if number < choice:
            print("Your number is too big")

        elif number > choice:
            print("Your number is too small")

        else:
            print(f"You win! Correct number is {number}")
            break

        if i == 10:
            print(f"You lose! Correct number is {number}")
            break


if __name__ == "__main__":
    guess_num()