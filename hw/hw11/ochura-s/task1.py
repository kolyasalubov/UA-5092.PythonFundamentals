def check_age(age):
    """
    This function returns a message stating whether the age is even or odd.
    Raises ValueError if the age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        return f"Your age {age} is even."
    return f"Your age {age} is odd."


try:
    user_age = int(input("Enter your age: "))
    print(check_age(user_age))
except ValueError as error:
    print(f"Error: {error}")
