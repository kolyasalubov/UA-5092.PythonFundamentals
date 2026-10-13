import math


# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# II. Find The Distance Between Two Points
def coordinates(p1, p2, precision=0):
    return round(math.hypot(p2[0] - p1[0], p2[1] - p1[1]), precision)


# III. No yelling!
def filter_words(st):
    return " ".join(st.split()).capitalize()


# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)


# V. Reversing Words in a String
def reverse_words(s):
    return " ".join(s.split()[::-1])


# VI. Reverse List Order
def reverse_list(lst):
    return lst[::-1]


# VII. Multiples of 3 or 5
def solution(number):
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)


# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    return name + " does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# XI. Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)


# XII. Is this my tail?
def correct_tail(body, tail):
    return body.endswith(tail)
