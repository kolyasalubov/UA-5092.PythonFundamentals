def get_number() -> int:
    """Get a number from user input."""
    return int(input("Enter a number (1-7): "))


def get_weekday(number: int) -> str:
    """Return the weekday corresponding to the number."""
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    return days.get(number, "Invalid day number")


def main() -> None:
    """Run the weekday checking program."""
    try:
        number = get_number()
        print(get_weekday(number))
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()