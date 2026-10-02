import operator

# task Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him slightly different. 
# She added a special case to her function, but she made a mistake.

def greet(name):
    '''
    This function takes a name as input and returns a greeting.
    If the name is "Johnny", it returns a special greeting.
    Otherwise, it returns a standard greeting.
    '''
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {0}!".format(name)

#task2
# Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    '''
    This function takes four coordinates as input and returns the distance between them.
    The distance is calculated using the Euclidean distance formula.
    The result is rounded to two decimal places.
    '''
    import math
    return round(math.dist((x1,y1),(x2,y2)),2)

#task3
# Write a function taking in a string like
#  WOW this is REALLY          amazing and
#  returning Wow this is really amazing.
#  String should be capitalized and properly spaced.

def filter_words(st):
    '''
    This function takes a string as input and returns a formatted string.
    The string is stripped of extra spaces, converted to lowercase, and capitalized.
    '''
    return " ".join(st.split()).lower().capitalize()

# task4
# We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know?

def number_to_string(num):
    '''
    This function takes an integer as input and returns it as a string.
    '''
    return f"{num}"

# task5
#  You need to write a function that reverses the words in a given string.
#  Words are always separated by a single space.
#  As the input may have trailing spaces, you will also need to
#  ignore unneccesary whitespace.

def reverse(st):
    '''
    This function takes a string as input and returns it with the words reversed.
    The string is split into words, reversed, and joined back together.
    '''
    st = st.split()
    st.reverse()
    return " ".join(st)

# task6
# In this kata you will create a function that takes in a list 
# and returns a list with the reverse order.

def reverse_list(l):
    '''
    This function takes a list as input and returns it with the elements in reverse order.
    '''
    l.reverse()
    return l

# task7
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples
#  of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If a number is a multiple of both 3 and 5, only count it once.

def solution(number):
    '''
    This function takes a number as input and returns the sum of all the multiples of 3 or 5 below that number.
    If the number is negative, it returns 0.
    '''
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# task8
# You were camping with your friends far away from home,
#  but when it's time to go back, you realize that your 
# fuel is running out and the nearest pump is 50 miles away!
#  You know that on average, your car runs on about 25 miles per gallon.
#  There are 2 gallons left.
# Considering these factors, write a function that tells
#  you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    '''
    This function takes the distance to the pump, miles per gallon, and fuel left as input.
    It returns True if it is possible to get to the pump with the fuel left, and False otherwise.
    '''
    return distance_to_pump / mpg <= fuel_left

# task9
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", 
# you are playing banjo!

def are_you_playing_banjo(name):
    '''
    This function takes a name as input and returns a string indicating whether the person plays banjo or not.
    If the name starts with "R" or "r", it returns "{name} plays banjo".
    Otherwise, it returns "{name} does not play banjo".
    '''
    return  f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"

# task10
# Complete the method that takes a boolean value and 
# return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    '''
    This function takes a boolean value as input and returns "Yes" if the value is True
    and "No" if the value is False.
    '''
    return "Yes" if boolean else "No"

# task11
# Consider an array/list of sheep where some sheep may be missing 
# from their place. We need a function that counts the number of 
# sheep present in the array (true means present).

def count_sheeps(sheeps):
    '''
    This function takes a list of boolean values as input and returns the count of True values in the list.
    '''
    return sheeps.count(True)

# task12
# Some new animals have arrived at the zoo. The zoo keeper is concerned 
# that perhaps the animals do not have the right tails. To help her,
#  you must correct the broken function to make sure that 
# the second argument (tail), is the same as the last letter of
#  the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.

def correct_tail(body, tail):
    '''
    This function takes a string (body) and a character (tail) as input.
    It returns True if the last character of the body matches the tail, and False otherwise.
    '''
    return body[-1] == tail

