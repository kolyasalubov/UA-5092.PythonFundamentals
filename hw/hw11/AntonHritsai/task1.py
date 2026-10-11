def process_age(age: int) -> None:
    """Validate the age and display whether it is even or odd.

    Args:
        age: The age to process.

    Raises:
        ValueError: If the age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative")

    result = "even" if age % 2 == 0 else "odd"
    print(f"Your age {age} is {result}")


if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        process_age(age)
    except ValueError as exc:
        print(exc)