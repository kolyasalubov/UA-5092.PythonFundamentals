import math


def greet(name):
    """Jenny's secret message"""
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


def distance(x1, y1, x2, y2):
    """Simple: Find The Distance Between Two Points"""
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


def filter_words(st):
    """No yelling!"""
    words = " ".join(st.lower().split())
    return f"{words[:1].upper()}{words[1:]}"


def number_to_string(num):
    """Convert a Number to a String!"""
    return str(num)


def reverse(st):
    """Reversing Words in a String"""
    return " ".join(reversed(st.split()))


def reverse_list(items):
    """Reverse List Order"""
    return list(reversed(items))


def solution(number):
    """Multiples of 3 or 5"""
    if number < 0:
        return 0
    result = 0
    for n in range(3, number):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return result


def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Will you make it?"""
    return fuel_left * mpg >= distance_to_pump


def are_you_playing_banjo(name):
    """Are You Playing Banjo?"""
    if name[:1].lower() == 'r':
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


def bool_to_word(boolean):
    """Convert boolean values to strings 'Yes' or 'No'."""
    return 'Yes' if boolean else 'No'


def count_sheeps(sheep):
    """Counting sheep..."""
    result = 0
    for s in sheep:
        if s:
            result += 1
    return result


def correct_tail(body, tail):
    """Is this my tail?"""
    sub = body[len(body) - len(tail):]
    return True if sub == tail else False
