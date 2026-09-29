import re


def validate_password(password: str):
    """
    Checks if the password is valid.
    """
    if len(password) < 6 or len(password) > 16:
        return False

    return re.search(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).*$",
        password
    )


if __name__ == "__main__":
    password = input("Enter your password: ")

    if validate_password(password):
        print("Password is correct")
    else:
        print("Password is incorrect")