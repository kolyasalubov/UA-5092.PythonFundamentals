DAYS_OF_WEEK = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_day(day_number: int) -> str:
    """
    Return the day of the week by its number.

    Args:
        day_number: The number of the day from 1 to 7.

    Returns:
        The corresponding day of the week.

    Raises:
        IndexError: If the number is less than 1 or greater than 7.
    """
    if day_number <= 0:
        raise IndexError("Number can't be negative or zero")

    if day_number > 7:
        raise IndexError("Number can't be greater than 7")

    return DAYS_OF_WEEK[day_number - 1]


def main() -> None:
    """
    Read user input and display the corresponding day of the week.

    Handles invalid numeric input and values outside the valid range.
    """
    try:
        user_input = int(input("Enter a number from 1 to 7: "))
        print(f"Day of the week: {get_day(user_input)}")
    except ValueError:
        print("Error: input must be a number")
    except IndexError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()