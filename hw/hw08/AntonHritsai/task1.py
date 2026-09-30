import re


def validate_password(password: str) -> list[str]:
    """Check if the given password meets the specified criteria.

    Args:
        password (str): The password to be validated.

    Returns:
        list[str]: A list of password validation errors.
    """
    errors = []

    if len(password) < 6:
        errors.append("Password must contain at least 6 characters.")

    if len(password) > 16:
        errors.append("Password must contain no more than 16 characters.")

    if not re.search(r"[a-z]", password):
        errors.append(
            "Password must contain at least 1 lowercase letter a-z."
        )

    if not re.search(r"[A-Z]", password):
        errors.append(
            "Password must contain at least 1 uppercase letter A-Z."
        )

    if not re.search(r"[0-9]", password):
        errors.append("Password must contain at least 1 number 0-9.")

    if not re.search(r"[$#@]", password):
        errors.append(
            "Password must contain at least 1 special character $#@."
        )

    if re.search(r"[^A-Za-z0-9$#@]", password):
        errors.append("Password contains unsupported characters.")

    return errors


def menu() -> None:
    """Menu for password validation."""
    while True:
        password = input(
            "Enter your password or nothing if you want to exit: "
        )
        if not password:
            break

        errors = validate_password(password)

        if not errors:
            print("Password is valid.")
        else:
            for error in errors:
                print(error)


if __name__ == "__main__":
    menu()