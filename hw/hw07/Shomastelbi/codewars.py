#task 1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#task 2

def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)

#task 3

def filter_words(st):
    st = st.lower().capitalize()
    return " ".join(st.split())

#task 4

def number_to_string(num):
    return str(num)

#task 5

def reverse(st):
    return " ".join(st.split()[::-1])

#task 6

def reverse_list(l):
    return l[::-1]

#task 7

def solution(number):
    summary = 0
    if number < 0:
        return 0
    for counter in range(0, number):
        if counter % 3 == 0 or counter % 5 == 0:
            summary += counter
    return summary

#task 8

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg <= fuel_left:
        return True
    return False

#task 9

def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo"
    return name + " does not play banjo"

#task 10

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

#task 11

def count_sheeps(sheep):
    counter = 0
    for present in sheep:
        if present:
            counter += 1
    return counter

#task 12

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    return False
