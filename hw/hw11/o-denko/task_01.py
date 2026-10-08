import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("file.log")
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)


def check_age(age: int) -> str:
    """
    Return 'even' or 'odd' for a non-negative age; raise ValueError if negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return "even" if age % 2 == 0 else "odd"


def main() -> None:
    """
    Prompt for user age, validate via check_age(), and print outcome or error.
    """
    user_input = input("Enter your age: ")
    try:
        age = int(user_input)
    except ValueError:
        logger.error("Non-integer input: %r", user_input)
        print("Invalid input: please enter a whole number.")
        return

    try:
        parity = check_age(age)
    except ValueError as error:
        logger.error("Invalid age %d: %s", age, error)
        print(f"Invalid age: {error}")
    else:
        print(f"Age is an {parity} number.")

if __name__ == "__main__":
    main()
