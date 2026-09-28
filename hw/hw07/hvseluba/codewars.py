# Task: Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

# Task: Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

# Task: Write a function taking in a string like WOW this is REALLY          amazing
# and returning Wow this is really amazing.
# String should be capitalized and properly spaced.

def filter_words(st):
    return " ".join(st.split()).capitalize()

# Task: We need a function that can transform a number (integer) into a string.

def number_to_string(num):
    return str(num)

# Task: You need to write a function that reverses the words in a given string.
# Words are always separated by a single space. 
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

def reverse(st):
    return " ".join(st.split()[::-1])

# Task: In this kata you will create a function that takes in a list
# and returns a list with the reverse order.

def reverse_list(l):
    return l[::-1]

# Task: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Finish the solution so that it returns
# the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0. Note: If a number is a multiple of both 3 and 5, only count it once.

def solution(number):
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    
    return total

# Task: You were camping with your friends far away from home, but when it's time to go back,
# you realize that your fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return (mpg * fuel_left) >= distance_to_pump

# Task: Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"

# Task: Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Task: Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#  True,  True,  True,  True ,
#  True,  False, True,  False,
#  True,  False, False, True ,
#  True,  True,  True,  True ,
#  False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    return sum(i for i in sheep if i is True)

# Task: Some new animals have arrived at the zoo.
# The zoo keeper is concerned that perhaps the animals do not have the right tails.
# To help her, you must correct the broken function to make sure that the second argument (tail),
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.

def correct_tail(body, tail):
    return body[-1] == tail
