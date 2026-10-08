from random import randint

def main() -> None:
    """
    Run a number guessing game with a maximum of ten attempts
    """
    secret_number = randint(1, 100)
    attempts = 0

    print("Вгадайте число від 1 до 100. Ви маєте 10 спроб")

    while attempts < 10:
        try:
            guess = int(input(f"Спроба {attempts + 1}: "))
        except ValueError:
            print("Введіть ціле число")
            continue

        if not 1 <= guess <= 100:
            print("Введіть число від 1 до 100")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Круто! Ви вгадали число за {attempts} спроб")
            return
        elif guess < secret_number:
            print("Загадане число більше")
        else:
            print("Загадане число менше")

    print(f"Спроби закінчилися. Загадане число: {secret_number}.")


if __name__ == "__main__":
    main()