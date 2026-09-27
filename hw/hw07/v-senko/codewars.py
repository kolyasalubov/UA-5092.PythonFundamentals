# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    
    return f"Hello, {name}!"



import math


# Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.
def distance(x1, y1, x2, y2):
    x_diff = x2 - x1
    y_diff = y2 - y1
    
    return round(math.sqrt((x_diff ** 2) + (y_diff ** 2)), 2)


# Write a function taking in a string like WOW this is REALLY 
# amazing and returning Wow this is really amazing. String should be capitalized and properly spaced.
def filter_words(st):
    
    return " ".join(st.split()).capitalize()


# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
def number_to_string(num):
    return f'{num}'


# You need to write a function that reverses the words in a given string. Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
def reverse(st):
    str_list = st.split()
    str_list.reverse()
    
    # Your Code Here
    return " ".join(str_list)


# In this kata you will create a function that takes in a list and returns a list with the reverse order.
def reverse_list(l):
    l.reverse()
    
    return l


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If a number is a multiple of both 3 and 5, only count it once.

# Courtesy of projecteuler.net (Problem 1)
def solution(number):
    sum = 0
    
    for item in range(1, number):
        if (item % 3 == 0 or item % 5 == 0):
            sum += item
    
    return sum


# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    range_left = fuel_left * mpg
    
    return range_left >= distance_to_pump


# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
def are_you_playing_banjo(name):
    lower_case_name = name.lower()
    
    if lower_case_name.startswith('r'):
        return f'{name} plays banjo'
    
    return f'{name} does not play banjo'


# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    return "Yes" if boolean else 'No'


# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
def count_sheeps(sheep):
    count = 0
    
    for item in sheep:
        count += 1 if item else 0
        
    return count

# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.
def correct_tail(body, tail):
    return body[-1] == tail[0]
