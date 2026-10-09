def division_calculator(values: str) -> float:
    """
    Split the input string by comma, convert components to float, and perform division.

    Args:
        values (str): A string containing two numbers separated by a comma.

    Raises:
        ValueError: If parsing or float conversion fails.
        ZeroDivisionError: If the second number evaluates to zero.

    Returns:
        float: The result of dividing the first number by the second number.
    """
    a, b = values.replace(" ", "").split(",")
    return float(a) / float(b)

if __name__ == "__main__":
    try:
        user_input = input("Enter two numbers separated by comma: ")
        result = division_calculator(user_input)
    except ValueError:
        print("You should enter two numbers separated by comma (e.g., 1,2)!")
    except ZeroDivisionError:
        print("Second number cannot be 0!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed!")
