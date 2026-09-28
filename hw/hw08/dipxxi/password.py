import re

def check(password: str) -> bool:
    """Перевіряє пароль на відповідність вимогам безпеки.

    Повертає True, якщо пароль валідний, і False, якщо ні.
    """
    if not (6 <= len(password) <= 16):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[$#@]", password):
        return False

    return True


if __name__ == "__main__":
    user_pass = input("Enter your password: ")

    if check(user_pass):
        print("Your password is valid.")
    else:
        print("Your password is invalid. ")

