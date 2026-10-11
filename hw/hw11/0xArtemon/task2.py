days = {
    1: "Monday", 
    2: "Tuesday", 
    3: "Wednesday", 
    4: "Thursday", 
    5: "Friday", 
    6: "Saturday", 
    7: "Sunday"
}

def convert_number_to_day(number: str) -> str:
    """
    Convert a given day number into its corresponding day of the week.

    Args:
        number (str): The day number entered by the user.

    Raises:
        ValueError: If the number is not between 1 and 7, or if non-numerical data is entered.

    Returns:
        str: A message stating the corresponding day of the week.
    """
    if 1 <= int(number) <= 7:
        return f"The {int(number)} day of the week is {days[int(number)]}!"
    else:
        raise ValueError

if __name__ == "__main__":
    try:
        print(convert_number_to_day(input("Enter day number: ")))
    except ValueError:
        print("You should enter a number between 1 and 7!")
