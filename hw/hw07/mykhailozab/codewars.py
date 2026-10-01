#Task1
#Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#Task2
#Given two ordered pairs calculate the distance between them.
# Round to two decimal places. 
#This should be easy to do in 0(1) timing.
import math
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

#Task3
#Write a function taking in a string like 
# WOW this is REALLY          amazing and returning Wow this is really amazing. 
# String should be capitalized and properly spaced.
def filter_words(st):
    return " ".join(st.capitalize().split())

#Task4
#We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know?

def number_to_string(num):
    str_c= ""
    return str_c + str(num)

#Task5
#You need to write a function that reverses the words in a given string. 
#Words are always separated by a single space.
#As the input may have trailing spaces, 
# you will also need to ignore unneccesary whitespace.

def reverse(st):
    return " ".join(st.split()[::-1])

#Task6
#In this kata you will create a function that takes
#in a list and returns a list with the reverse order.

def reverse_list(l):
    l.reverse()
    return l

#Task7
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
#Finish the solution so that it returns 
#the sum of all the multiples of 3 or 5 below the number passed in.
#Additionally, if the number is negative, return 0.
#Note: If a number is a multiple of both 3 and 5, only count it once.

def solution(number):
    suma = 0
    for i in range(1,number):
        if i < 0:
            suma == 0
        elif i % 3 == 0:
            suma +=i
        elif i % 5 == 0:
            suma +=i
    return suma

#Task9
#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#Task10
#Complete the method that takes a boolean value and
#return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"

#Task11
#Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts
# the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    sum = 0
    for i in sheep:
        if i == True:
            sum += 1
        elif i == False:
            pass
    return sum

#Task12
#Some new animals have arrived at the zoo.
#The zoo keeper is concerned that perhaps the animals do not have
#the right tails. To help her, you must correct
#the broken function to make sure that the second argument (tail),
#is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#If the tail is right return true, else return false.
#The arguments will always be non empty strings, and normal letters.

def correct_tail(body, tail):
    if body[-1].lower == tail[0].lower:
        return True
    else:
        return False


