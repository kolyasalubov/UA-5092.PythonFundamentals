from custom_exceptions import NegativeAgeError
from logger import logger


def process_age(age: int) -> str:
    """
    Process age and return whether it is even or odd.
    Args:
        age: the age as int to process.
    Returns:
        A message as str stating whether the age is even or odd.
    Raises:
        NegativeAgeError: If the age is negative.
    """
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")

    if age % 2 == 0:
        logger.info(f"The age {age} is even.")
        return f"The age {age} is even."
    else:
        logger.info(f"The age {age} is odd.")
        return f"The age {age} is odd."


def main() -> None:
    """Run the age processing program."""
    try:
        age = int(input("Please enter your age: "))
        logger.info(f"User's age is {age}.")
        print(process_age(age))
    except NegativeAgeError as error:
        logger.error(error)
    except ValueError:
        logger.error("Invalid input.")


if __name__ == "__main__":
    main()
