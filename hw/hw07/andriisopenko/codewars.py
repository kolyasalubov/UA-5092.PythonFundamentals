# 1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, " + name + "!"


# 2
def distance_between_points(a, b):
    return round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5, 2)


# 3
def filter_words(st):
    return " ".join(st.split()).capitalize()


# 4
def number_to_string(num):
    return str(num)


# 5
def reverse(st):
    return " ".join(st.split()[::-1])


# 6
def reverse_list(l):
    return l[::-1]


# 7
def solution(number):
    result = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


# 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


# 9
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    return name + " does not play banjo"


# 10
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"


# 11
def count_sheeps(sheep):
    return sheep.count(True)


# 12
def correct_tail(body, tail):
    return body[-1] == tail