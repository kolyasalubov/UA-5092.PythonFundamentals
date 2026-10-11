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

DAYS: dict[int, str] = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def get_day_of_week(day_number: int) -> str:
    """
    Return day name for a number (1-7); raise ValueError if out of range.
    """
    day_name = DAYS.get(day_number)
    if day_name is None:
        raise ValueError("Day number must be between 1 and 7.")
    return day_name


def main() -> None:
    """
    Prompt user for a day number, validate input, and print day name or error.
    """
    user_input = input("Enter day number (1-7): ")
    try:
        day_number = int(user_input)
        day_name = get_day_of_week(day_number)
    except ValueError as error:
        logger.error("Invalid day input %r: %s", user_input, error)
        print(f"Invalid input: {error}")
    else:
        print(f"Day of the week: {day_name}")


if __name__ == "__main__":
    main()
