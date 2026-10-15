"""
Task 1
Fix the greeting function for Jenny and Johnny.
"""

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


"""
Task 2
Calculate the distance between two points and round to 2 decimals.
"""
import math

def distance(x1, y1, x2, y2):
    """
    Обчислює відстань між чотирма координатами x1, y1, x2, y2.
    Складність за часом: O(1).
    """
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


"""
Task 3
Normalize spaces and capitalization in a string.
"""

def format_string(text):
    """Виправляє регістр і зайві пробіли в рядку."""
    return " ".join(text.lower().split()).capitalize()


"""
Task 4
Convert an integer to a string.
"""

def number_to_string(number):
    """Перетворює ціле число на рядок."""
    return str(number)


"""
Task 5
Reverse the words in a string and remove extra spaces.
"""

def reverse_words(text):
    """Перевертає порядок слів у рядку та прибирає зайві пробіли."""
    return " ".join(text.strip().split()[::-1])


"""
Task 6
Write a function that reverses a list.
"""

def reverse_list(items):
    """Повертає список у зворотному порядку."""
    return items[::-1]


"""
Task 7
Find the sum of all multiples of 3 or 5 below a given number.
"""

def solution(number):
    """Повертає суму чисел, кратних 3 або 5."""
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


"""
Task 8
Check if the car can reach the pump with the available fuel.
"""

def zero_fuel(distance, mpg, fuel):
    """Перевіряє, чи вистачить пального, щоб доїхати до заправки."""
    return fuel * mpg >= distance


"""
Task 9
Check whether a name starts with the letter R.
"""

def are_you_playing_banjo(name):
    """Перевіряє, чи починається ім'я з літери R."""
    if name.startswith(("R", "r")):
        return name + " plays banjo"
    return name + " does not play banjo"


"""
Task 10
Return "Yes" for True and "No" for False.
"""

def bool_to_word(value):
    """Перетворює логічне значення на слово."""
    return "Yes" if value else "No"


"""
Task 11
Count the number of True values in a list.
"""

def count_sheeps(sheep):
    """Підраховує кількість присутніх овець."""
    return sum(sheep)


"""
Task 12
Check if the animal’s tail matches the last letter of its name.
"""

def correct_tail(body, tail):
    """Перевіряє, чи збігається хвіст з останньою літерою назви."""
    return body[-1] == tail

