# 1. Jenny's secret message. Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# 2.Find The Distance Between Two Points. Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.
import math
def distance(x1, y1, x2, y2):
   return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)

# 3.No yelling!Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. String should be capitalized and properly spaced.
def filter_words(st):
     return " ".join(st.split()).capitalize()

# 4.Convert a Number to a String! We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)

#5.Reversing Words in a String. You need to write a function that reverses the words in a given string. Words are always separated by a single space.
def reverse(st):
    return " ".join(st.split()[::-1])

#6.Reverse List Order. In this kata you will create a function that takes in a list and returns a list with the reverse order.
def reverse_list(l):
    return l[::-1]

#7.Multiples of 3 or 5. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#Additionally, if the number is negative, return 0.
def solution(number):
    return sum(n for n in range(number)
               if n % 3 == 0 or n % 5 == 0)

#8.Will you make it? You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
#Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#9.Are You Playing Banjo? Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
def are_you_playing_banjo(name):
    if name.startswith(("R", "r")):
        return name +" plays banjo"
    return name +" does not play banjo"

#10. Convert boolean values to strings 'Yes' or 'No'. Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

#11. Counting sheep. Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
def count_sheeps(sheep):
  return sum(item is True for item in sheep)

#12. Is this my tail? Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#If the tail is right return true, else return false.
def correct_tail(body, tail):
     return body[-1] == tail