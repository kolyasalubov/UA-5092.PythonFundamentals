import re


def is_password_valid(password: str) -> bool:
    """Check if the given password meets the specified criteria.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$"
    return bool(re.match(pattern, password))


def menu() -> None:
    """Menu for password validation."""
    while True:
        password = input("Enter your password or nothing if you want to exit: ")
        if not password:
            break
        if is_password_valid(password):
            print("Password is valid.\n")
        else:
            print(
                """Password is invalid.
It must contain at least 1 lowercase letter a-z
It must contain at least 1 uppercase letter A-Z
It must contain at least 1 number 0-9
It must contain at least 1 special character $#@
Total length must be between 6 and 16 characters
"""
            )


if __name__ == "__main__":
    menu()