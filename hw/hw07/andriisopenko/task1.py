def largest_number(first: float, second: float) -> float:
    """Return the largest of two numbers."""
    if first > second:
        return first
    return second
print(largest_number(10, 20))