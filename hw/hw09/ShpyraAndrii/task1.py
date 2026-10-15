from random import randint

MAX_ATTEMPTS = 10
MAX_NUMBER = 100
MIN_NUMBER = 1


def main():
    attempts = MAX_ATTEMPTS
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    while attempts > 0:
        prompt = (
            f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER} "
            f"({attempts} left): "
        )
        try:
            user_num = int(input(prompt))
        except ValueError:
            print("Incorrect value, please enter number")
            continue
        finally:
            attempts -= 1

        if user_num == random_number:
            print("You won")
            return
        elif not MIN_NUMBER <= user_num <= MAX_NUMBER:
            print(f"The number must be between {MIN_NUMBER} and {MAX_NUMBER}.")
        elif user_num > random_number:
            print("Incorrect, number is lower")
        else:
            print("Incorrect, number is higher")

    print(f"You lost, the correct answer was: {random_number}")


if __name__ == "__main__":
    main()
