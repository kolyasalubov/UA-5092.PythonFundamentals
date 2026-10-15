def check_age(age: str) -> str:
    """
    Check if the entered age is even or odd.

    Args:
        age (str): The age entered by the user.

    Raises:
        ValueError: If the entered number is negative or not a valid integer.

    Returns:
        str: A message stating whether the age is even or odd.
    """
    if int(age) >= 0:
        return f"Your age is {'even' if int(age) % 2 == 0 else 'odd'}!"
    else:
        raise ValueError
    
if __name__ == "__main__":
    try:
        print(check_age(input("Enter your age: ")))
    except ValueError:
        print("You should enter positive number!")
