# I. Jenny's secret message
def greet(name: str) -> str:
    """
    Greet person by name.
    Args: name - str
    Returns: str
    """
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2) -> float:
    """
    Calculate the distance between two points.
    Args: x1, y1, x2, y2 - int or float
    Returns: float
    """
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# III. No yelling!
def filter_words(st: str) -> str:
    """
    Normalize input string.
    Args: st - str
    Returns: str
    """
    normalized_st = st.strip().lower().capitalize()

    while "  " in normalized_st:
        normalized_st = normalized_st.replace("  ", " ")

    return normalized_st


# IV. Convert a Number to a String
def number_to_string(num: int) -> str:
    """
    Convert integer to string.
    Args: num - int
    Returns: str
    """
    return str(num)


# V. Reversing Words in a String
def reverse(st: str) -> str:
    """
    Reverse words in a string.
    Args: st - str
    Returns: str
    """
    list_st = st.strip().split()
    return " ".join(list_st[::-1])


# VI. Reverse List Order
def reverse_list(my_list: list) -> list:
    """
    Return a list with the reverse order.
    Args: my_list - list
    Returns: list
    """
    return my_list[::-1]


# VII. Multiples of 3 or 5
def solution(number: int) -> int:
    """
    Return the sum of all the multiples of 3 or 5 below the number passed in.
    Args: number - int
    Returns: int
    """
    if number < 0:
        return 0

    multiples = set()

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.add(i)

    return sum(multiples)


# VIII. Will you make it?
def zero_fuel(distance_to_pump: float,
              mpg: float,
              fuel_left: float) -> bool:
    """
    Verify if it is possible to get to the pump or not.
    Args:
        distance_to_pump - float
        mpg - float
        fuel_left - float
    Returns: bool
    """
    fuel_need = distance_to_pump / mpg
    return fuel_left >= fuel_need


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name: str) -> str:
    """
    Verify if a person plays banjo.
    Args: name - str
    Returns: str
    """
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean: bool) -> str:
    """
    Convert boolean values to strings 'Yes' or 'No'.
    Args: boolean - bool
    Returns: str
    """
    return "Yes" if boolean else "No"


# XI. Counting sheep
def count_sheep(sheep: list[bool]) -> int:
    """
    Count the number of sheep present in the list.
    Args: sheep - list[bool]
    Returns: int
    """
    return sheep.count(True)


# XII. Is this my tail?
def correct_tail(body: str, tail: str) -> bool:
    """
    Verify if 'body' ends with 'tail'.
    Args:
        body - str
        tail - str
    Returns: bool
    """
    return body.endswith(tail)
