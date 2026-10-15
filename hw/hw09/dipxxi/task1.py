from random import randint

SECRET_NUMBER = randint(1, 100)


def check_guess(guess):
    """Перевіряє введене число та порівнює його із загаданим.
    Повертає None, якщо числа рівні, True — якщо введене число більше,
    та False — якщо менше.
    """
    if guess == SECRET_NUMBER:
        return None
    return guess > SECRET_NUMBER


def your_lack(is_smaller=None, attempt=1):
    """Запускає ігровий процес рекурсивно до 10 спроб.
    Приймає підказку (is_smaller) та поточний номер спроби (attempt).
    """
    if attempt > 10:
        return print(f"Game over! Number was: {SECRET_NUMBER}")

    msg = (
        "Type your number:"
        if is_smaller is None
        else ("Try smaller:" if is_smaller else "Try bigger:")
    )
    user_beat = int(input(f"{msg} "))

    result = check_guess(user_beat)

    if result is None:
        return print("You win!")

    your_lack(result, attempt + 1)


if __name__ == "__main__":
    your_lack()


