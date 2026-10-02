import re

MIN_LENGTH = 6
MAX_LENGTH = 16

RULES = [
    (rf"^.{{{MIN_LENGTH},{MAX_LENGTH}}}$",
     f"it must be from {MIN_LENGTH} to {MAX_LENGTH} characters long"),
    (r"[a-z]", "it must contain at least one lowercase letter [a-z]"),
    (r"[A-Z]", "it must contain at least one uppercase letter [A-Z]"),
    (r"[0-9]", "it must contain at least one digit [0-9]"),
    (r"[$#@]", "it must contain at least one character from [$#@]"),
]


def check_password(password: str) -> list[str]:
    """Return a list of validation errors, empty if the password is valid.

    Args:
        password: the password to validate.

    Returns:
        A list of human-readable messages describing the unmet requirements.
    """
    return [message for pattern, message in RULES
            if not re.search(pattern, password)]


def is_valid_password(password: str) -> bool:
    """Return True if the password meets every requirement."""
    return not check_password(password)


if __name__ == "__main__":
    user_password = input("Enter a password: ")
    problems = check_password(user_password)

    if not problems:
        print("The password is valid.")
    else:
        print("The password is invalid:")
        for problem in problems:
            print(f"  - {problem}")
