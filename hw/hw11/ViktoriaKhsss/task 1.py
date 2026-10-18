def get_age() -> int:
    """Get the user's age from input."""
    age = int(input("Enter your age: "))
    return age


def check_age(age: int) -> None:
    """Check if the age is negative, even, or odd."""
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")


def main() -> None:
    """Run the age checking program."""
    age = get_age()
    check_age(age)


if __name__ == "__main__":
    main()