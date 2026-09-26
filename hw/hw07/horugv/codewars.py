# 1 - Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

# 2 - Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    calculate = math.sqrt((x2 - x1)**2+(y2 - y1)**2)
    return round(calculate, 2)

# 3 - No yelling!
def filter_words(st):
    str_to_array = st.split()
    return " ".join(str_to_array).lower().capitalize()

# 4 - Convert a Number to a String!
def number_to_string(num):
    return str(num)

# 5 - Reversing Words in a String
def reverse(st):
    st_to_array = st.split()
    st_to_array.reverse()
    return " ".join(st_to_array)

# 6 - Reverse List Order
def reverse_list(l):
    return l[::-1]

# 7 - Multiples of 3 or 5
def solution(number):
    sum = 0
    for item in range(int(number)):
        if (item % 3 == 0 or item % 5 == 0) and item > 0:
            sum += item
    return sum
  
# 8 - Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# 9 - Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0].lower() == "r" else name + " does not play banjo"

# 10 - Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# 11 - Counting sheep
def count_sheeps(sheep):
  return sheep.count(True)

# 12 - Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail[0]