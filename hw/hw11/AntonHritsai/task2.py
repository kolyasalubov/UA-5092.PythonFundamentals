DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def process_day(day: int) -> None:
    """Print the day of the week corresponding to the given number.

    Args:
        day: The number of the day.

    Raises:
        KeyError: If the day number is invalid.
    """
    if day not in DAYS:
        raise KeyError("Invalid day")

    print(DAYS[day])


if __name__ == "__main__":
    try:
        user_input = int(input("Enter the day: "))
        process_day(user_input)
    except ValueError:
        print("It must be a number")
    except KeyError as exc:
        print(exc.args[0])