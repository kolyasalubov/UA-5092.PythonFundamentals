import math

# 1
def greet(name):
    """Спеціальне привітання для Джонні"""
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# 2
def distance(x1, y1, x2, y2):
    """Обчислює відстань між двома точками"""
    x_diff = x2 - x1
    y_diff = y2 - y1
    result = math.sqrt((x_diff ** 2) + (y_diff ** 2))
    return round(result, 2)


# 3
def filter_words(st):
    """Прибирає зайві пробіли та форматує текст"""
    words = st.split()
    clean_str = " ".join(words)
    return clean_str.capitalize()


# 4
def number_to_string(num):
    """Перетворює число на рядок"""
    return f"{num}"


# 5
def reverse(st):
    """Розгортає порядок слів у рядку задом наперед"""
    str_list = st.split()
    str_list.reverse()
    return " ".join(str_list)


# 6
def reverse_list(l):
    """Розгортає список елементів задом наперед"""
    l.reverse()
    return l


# 7
def solution(number):
    """Рахує суму всіх чисел, кратних 3 або 5, менших за вказане число"""
    total_sum = 0
    for item in range(1, number):
        if item % 3 == 0 or item % 5 == 0:
            total_sum = total_sum + item
    return total_sum


# 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Перевіряє, чи вистачить палива до заправки"""
    range_left = fuel_left * mpg
    return range_left >= distance_to_pump


# 9
def are_you_playing_banjo(name):
    """Перевіряє, чи грає людина на банджо за першою літерою імені"""
    lower_case_name = name.lower()
    if lower_case_name.startswith('r'):
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


# 10
def bool_to_word(boolean):
    """Перетворює True на 'Yes', а False на 'No'"""
    if boolean:
        return "Yes"
    return "No"


# 11
def count_sheeps(sheep):
    """Рахує кількість овець у списку"""
    count = 0
    for item in sheep:
        if item:
            count = count + 1
    return count


# 12
def correct_tail(body, tail):
    """Перевіряє, чи правильно вказано останню літеру тварини"""
    return body[-1] == tail
