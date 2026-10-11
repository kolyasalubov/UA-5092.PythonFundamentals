import re

def validation(password: str) -> bool:
    """Check whether a password meets all validation requirements.
    Require 6–16 characters, at least one lowercase letter,
    one uppercase letter, one digit, and one character from $#@
    """
    if not 6 <= len(password) <= 16:
        return False

    patterns = (r"[a-z]", r"[A-Z]", r"[0-9]", r"[$#@]")

    return all(re.search(pattern, password) is not None
               for pattern in patterns)

def main() -> None:
    """
    Prompt the user for a password and print its validation result
    """
    password = input("Введіть пароль: ")

    if validation(password):
        print("Пароль правильний")
    else:
        print("Пароль неправильний")


if __name__ == "__main__":
    main()