class InvalidAgeError(Exception):
    """Raised when the entered age is invalid."""
    pass


def check_age(user_input: str) -> str:
    """
    Check whether the entered age is valid and determine if it is even or odd.

    Args:
        user_input: The age entered by the user as a string.

    Returns:
        A message indicating whether the age is even or odd.

    Raises:
        InvalidAgeError: If the input is not a number or the age is negative.
    """
    try:
        age = int(user_input)
    except ValueError:
        raise InvalidAgeError("Age must be a number")

    if age < 0:
        raise InvalidAgeError("Age can't be negative")

    if age % 2 == 0:
        return "Age is Even"

    return "Age is Odd"


def main() -> None:
    """
    Ask the user to enter their age and display whether it is even or odd.

    Handles InvalidAgeError if the entered age is invalid.
    """
    try:
        user_input = input("Input your age: ")
        print(check_age(user_input))
    except InvalidAgeError as exc:
        print(exc)


if __name__ == "__main__":
    main()