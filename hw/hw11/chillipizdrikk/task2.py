"""Module for checking whether a day of the week corresponds to it`s number"""

WEEK_DAYS: dict[int, str] = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

class InvalidDayError(Exception):
    """Raised when a number does not correspond to a day of the week."""

def week_day(number: int) -> str:
    """Return the name of the weekday for the given number.
    Args:
        number: The day number.
    Returns:
        The name of the corresponding weekday.
    Raises:
        InvalidDayError: If the number is not in the range 1-7.
    """
    if number not in WEEK_DAYS:
        raise InvalidDayError(f"Number {number} is not a day of the week (expected 1-7).")
    return WEEK_DAYS[number]

def main() -> None:
    """Prompt user for a day number and print the weekday. 
    Also handles errors.
    """
    while True:
        try:
            user_input = input("Enter number of the day or 'exit' to leave: ").strip()
            if user_input == "exit":
                print("Bye!")
                break

            number = int(user_input)
            result = week_day(number)
        except ValueError:
            print(f"Error: Input must be a whole number.")
        except InvalidDayError as e:
                print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            print(result)

if __name__ == "__main__":
    main()