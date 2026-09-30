def validate_input_values(*args: str) -> tuple[float, ...] | None:
    """Validate the input values.

    Args:
        *args: The input values to validate.

    Returns:
        A tuple of float values if all values are valid and greater than 0,
        otherwise None.
    """
    try:
        values = tuple(float(i) for i in args)
    except ValueError:
        return None

    for value in values:
        if value <= 0:
            return None

    return values