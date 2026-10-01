import random

def random_number() -> int:
    """
    Generate a random integer from 1 to 100.

    Returns:
        int: A random integer between 1 and 100.
    """
    return random.randint(1,100)


def main() -> None:
    counter = 0
    number = random_number()
    while counter < 10:
        try:
            user_number = int(input("Input your number: "))
        except ValueError:
            print("Invalid option")
            continue
        if user_number > number:
            counter += 1
            print(f"The number is less than {user_number}")
            continue
        elif user_number < number:
            counter += 1
            print(f"The number is greater than {user_number} ")
            continue
        elif user_number == number:
            print(f"You guessed the number {number}!")
            break
    if counter <= 10:
        print("You have used all your attempts")

if __name__ == "__main__":
    main()