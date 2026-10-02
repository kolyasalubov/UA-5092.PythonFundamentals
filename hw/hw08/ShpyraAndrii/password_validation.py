import re


def is_valid_password(password: str) -> bool:
    """
        Програма на Python для перевірки валідності пароля.
        Вимоги до перевірки:
        ➢ Щонайменше 1 мала літера в діапазоні [a-z]
        ➢ Щонайменше 1 велика літера в діапазоні [A-Z].
        ➢ Щонайменше 1 цифра в діапазоні [0-9].
        ➢ Щонайменше 1 символ із набору [$#@].
        ➢ Мінімальна довжина — 6 символів.
        ➢ Максимальна довжина — 16 символів
    """
    result = re.fullmatch(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$",
        password)
    return result is not None


if __name__ == '__main__':
    password = input("Please enter your password for validation: ").strip()
    is_valid = is_valid_password(password)
    print(f"Your password is {'valid' if is_valid else 'invalid'}")
