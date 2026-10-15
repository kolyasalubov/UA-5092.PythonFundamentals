# Task 1:
def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"

# Task 2:
import math
def distance(x1, y1, x2, y2):
    return round(math.hypot(x2 - x1, y2 - y1), 2)

# Task 3: 
def filter_words(st):
    return " ".join(st.capitalize().split())

# Task 4: 
def number_to_string(num):
    return str(num)

# Task 5:
def reverse(st):
    return " ".join(st.split()[::-1])

# Task 6:
def reverse_list(l):
    return l[::-1]

# Task 7: 
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0) if number > 0 else 0

# Task 8:
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# Task 9:
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"

# Task 10: 
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Task 11: 
def count_sheeps(sheep):
    return sheep.count(True)

# Task 12: 
def correct_tail(body, tail):
    return body.endswith(tail)