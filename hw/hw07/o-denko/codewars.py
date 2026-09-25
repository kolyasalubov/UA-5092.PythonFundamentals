# Task 1: Jenny's secret message 
# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him 
# slightly different. She added a special case to her function, 
# but she made a mistake.


def greet(name: str) -> str:
    """
    Return a personalized greeting, with a special case for Johnny.
    """
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# Task 2: Find The Distance Between Two Points 
# Given two ordered pairs calculate the distance between them. 
# Round to two decimal places. This should be easy to do in 0(1) timing.


def distance(x1: float | int, y1: float | int, x2: float | int, y2: float | int) -> float:
    """
    Calculate the Euclidean distance between two points rounded to two decimal places.
    """
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(d, 2)


# Task 3: No yelling!
# Write a function taking in a string like WOW this is REALLY
# amazing and returning Wow this is really amazing. String should be 
# capitalized and properly spaced.


def filter_words(st: str) -> str:
    """
    Capitalize a sentence and normalize internal whitespace.
    """
    return ' '.join(st.split()).capitalize()


# Task 4: Convert a Number to a String
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?


def number_to_string(num: int | float) -> str:
    """
    Convert a number into its string representation.
    """
    return str(num)


# Task 5: Reversing Words in a String
# You need to write a function that reverses the words in a given string. 
# Words are always separated by a single space.
# As the input may have trailing spaces, you will also need 
# to ignore unneccesary whitespace.


def reverse(st: str) -> str:
    """
    Reverse the order of words in a string.
    """
    words = st.split()
    words.reverse()
    return ' '.join(words)



# Task 6: Reverse List Order
# In this kata you will create a function that 
# takes in a list and returns a list with the reverse order.


def reverse_list(items: list) -> list:
    """
    Return a list in reverse order.
    """
    return items[::-1]


# Task 7: Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples 
# of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If a number is a multiple of both 3 and 5, only count it once.


def solution(number: int) -> int:
    """
    Return the sum of all natural multiples of 3 or 5 below the given number.
    """
    if number <= 0: 
        return 0

    total = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total


# Task 8: Will you make it?
# You were camping with your friends far away from home, but when it's 
# time to go back, you realize that your fuel is running out and the nearest 
# pump is 50 miles away! You know that on average, your car runs on about
# 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible 
# to get to the pump or not.
# Function should return true if it is possible and false if not.


def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    """
    Check if remaining fuel is sufficient to reach the destination.
    """
    return mpg * fuel_left >= distance_to_pump


# Task 9: Are You Playing Banjo?
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:


def are_you_playing_banjo(name: str) -> str:
    """
    Determine if a person plays banjo based on the first letter of their name.
    """
    if name.lower().startswith("r"):
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


# Task 10: Convert boolean values to strings 'Yes' or 'No’
# Complete the method that takes a boolean value and return 
# a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean: bool) -> str:
    """
    Convert a boolean value to 'Yes' or 'No' string.
    """
    return "Yes" if boolean else "No"


# Task 11: Counting sheep
# Consider an array/list of sheep where some sheep may be missing
# from their place. We need a function that counts the number of sheep 
# present in the array (true means present).


def count_sheeps(sheep: list[bool]) -> int:
    """
    Count the number of present sheep in a given list.
    """
    return sheep.count(True)


# Task 12: Is this my tail?
# Some new animals have arrived at the zoo. The zoo keeper is concerned 
# that perhaps the animals do not have the right tails. To help her, you 
# must correct the broken function to make sure that the second argument
#  (tail), is the same as the last letter of the first argument (body) - 
# otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.


def correct_tail(body, tail):
    """
    Check whether the tail matches the last character of the body.
    """
    return body.endswith(tail)[-1] == tail
