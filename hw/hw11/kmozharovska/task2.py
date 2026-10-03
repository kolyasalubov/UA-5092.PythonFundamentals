from custom_exceptions import OutOfBoundsException
from logger import logger

WEEK = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def process_weekday(number: int) -> str:
    """
    Process number and return the day of the week.
    Args:
        number: int to process.
    Returns:
        Day of the week as str.
    Raises:
        OutOfBoundsException: if number is out of 1-7 range.
    """
    if number not in WEEK:
        raise OutOfBoundsException(number)
    day_of_week = WEEK[number]
    logger.info(f"{number} is {day_of_week}.")
    return day_of_week


def main() -> None:
    """Run the number processing program."""
    try:
        number = int(input("Please enter a number between 1 and 7: "))
        print(process_weekday(number))
    except OutOfBoundsException as error:
        logger.error(error)
    except ValueError:
        logger.error("Invalid input.")


if __name__ == "__main__":
    main()
