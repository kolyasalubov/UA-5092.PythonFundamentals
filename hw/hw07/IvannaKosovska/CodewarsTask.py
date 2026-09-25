#task1: Jenny's secret message

def greet(name):
    """
    Function returns a standard greeting for all users except Johnny.
    """
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)


#task2: Find The Distance Between Two Points

import math

def distance(x1, y1, x2, y2):
    """
    Function calculates the distance between given points. Round to two decimal places.
    """
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

#task3: No yelling!

def filter_words(st):
    """
    Function converts the string into list of words,
    join with a single space using the join function and capitalize the phrase.
    """
    return " ".join(st.split()).capitalize()

#task4: Convert a Number to a String!

def number_to_string(num):
    """
    Function converts a Number to a String
    """
    return str(num)

#task5: Reversing Words in a String
def reverse(st):
    """
    This function create the list of words in given phrase, reverses list items 
    and then joins them with single space.
    """
    return " ".join(st.split()[::-1])

#task6: Reverse List Order
def reverse_list(l):
    """
    return a list with the reverse order of l'
    """
    return l[::-1]

def reverse_list(l):
    return l.reverse()

#task7: Multiples of 3 or 5

def solution(number):
    """
    if the number is negative, return 0
    """
    if number <= 0:
        return 0
    total = 0
    while number != 0:
        number -= 1
        if number % 3 == 0 or number % 5 == 0:
            total += number
    return total

#task8: Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

#task9: Are You Playing Banjo?

def are_you_playing_banjo(name):
    return name + " plays banjo" if name.lower().startswith("r") else name + " does not play banjo"

#task10: Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#task11: Counting sheep...

def count_sheeps(sheep):
    return sheep.count(True)

#task12: Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail

def correct_tail(body, tail):
    return body.endswith(tail)