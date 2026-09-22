import math

""" Jenny's secret message """

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


""" Simple: Find The Distance Between Two Points """

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2),2)

""" No yelling! """ 

def filter_words(st):
    words =" ".join(st.lower().split())
    return f"{words[:1].upper()}{words[1:]}"

""" Convert a Number to a String! """

def number_to_string(num):
    return str(num)

""" Reversing Words in a String """

def reverse(st):
    return " ".join(reversed(st.split()))

""" Reverse List Order """

def reverse_list(l):
    return list(reversed(l))


""" Multiples of 3 or 5 """

def solution(number):
    if number < 0:
        return 0
    result = 0
    for n in range(3, number):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return result
        
"""  Will you make it? """
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

""" Are You Playing Banjo? """
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[:1].lower() == 'r' else f"{name} does not play banjo"

""" Convert boolean values to strings 'Yes' or 'No'. """
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

""" Counting sheep... """

def count_sheeps(sheep):
    result = 0
    for s in sheep:
        if s: result+=1
    return result

""" Is this my tail? """

def correct_tail(body, tail):
     sub = body[len(body)-len(tail):]
     return True if sub == tail else False
