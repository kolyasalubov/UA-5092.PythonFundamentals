import re

MIN_LENGTH = 6
MAX_LENGTH = 16

RE_LOWERCASE = re.compile(r"[a-z]")
RE_UPPERCASE = re.compile(r"[A-Z]")
RE_DIGIT = re.compile(r"[0-9]")
RE_SPECIAL = re.compile(r"[$#@]")


def is_valid_password(password: str) -> bool:
    """Check if all password conditions are met."""
    rules = (
        MIN_LENGTH <= len(password) <= MAX_LENGTH,
        RE_LOWERCASE.search(password) is not None,
        RE_UPPERCASE.search(password) is not None,
        RE_DIGIT.search(password) is not None,
        RE_SPECIAL.search(password) is not None,
    )
    return all(rules)


if __name__ == "__main__":
    print("Password requirements:")
    print(f"- Length: {MIN_LENGTH} to {MAX_LENGTH} characters")
    print("- At least one lowercase letter [a-z]")
    print("- At least one uppercase letter [A-Z]")
    print("- At least one digit [0-9]")
    print("- At least one special character from [$#@]\n")

    user_password = input("Enter your password: ")

    if is_valid_password(user_password):
        print("Password is valid!")
    else:
        print("Password does not meet the requirements. Please check the rules above and try again.")
