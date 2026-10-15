DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def day_of_week(number):
    """
    This function returns the day of the week for a number from 1 to 7.
    Raises IndexError if the number is out of range.
    """
    if number < 1:
        raise IndexError
    return DAYS[number - 1]


try:
    day_number = int(input("Enter a day number (1-7): "))
    print(day_of_week(day_number))
except ValueError:
    print("Error: please enter a whole number, not text.")
except IndexError:
    print("Error: there are only 7 days in a week, enter a number from 1 to 7.")
