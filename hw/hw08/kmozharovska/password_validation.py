import re

"""
The module provides a function to check whether a password
meets the required length and character requirements.
"""
PASSWORD_PATTERN = (
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])"
    r"[A-Za-z0-9$#@]{6,16}$"
)


def is_valid_password(password: str) -> bool:
    """
    Check whether a password is valid.
    Args: password - str
    Returns: bool
    """
    return bool(re.match(PASSWORD_PATTERN, password))


if __name__ == '__main__':
    while True:
        password = input("Enter your password: ")

        if is_valid_password(password):
            print("Your password is valid.")
            break
        else:
            print("Your password is invalid. "
                  "The password must contain at least one lowercase letter, "
                  "one uppercase letter, one digit, one of $, #, @ symbols, "
                  "and be between 6 and 16 characters long. Try again.")
