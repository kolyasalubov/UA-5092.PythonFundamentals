"""Module for checking whether an age is even or odd"""


class NegativeAgeError(Exception):
    """Class that raise exception when the user enters a negative age."""
    pass


def check_even(age: int) -> str:
    """Determine whether the given age is even or odd.
    Args:
        age: User's age.
    Returns:
        Message stating whether the age is even or odd.
    Raises:
        NegativeAgeError: If the age is negative.
    """
    if age < 0:
        raise NegativeAgeError("Age can`t be negative!")
    if age % 2 == 0:
        return f"{age} is even."
    else:
        return f"{age} is odd."


def main() -> None:
    """Prompt the user for their age and print whether
    it is even or odd. Also handles errors.
    """
    try:
        age = int(input("Enter your age: "))
        result = check_even(age)
    except NegativeAgeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print("Incorrect input: please enter a whole number.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print(result)

if __name__ == "__main__":
    main()