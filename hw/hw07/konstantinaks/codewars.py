# # task1

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {0}!".format(name)

# # task2

# import math
# def distance(x1, y1, x2, y2):
#     return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

# # task 3

# def filter_words(st):
#     result = st.split()
#     clean_text = " ".join(result)
#     res = clean_text.capitalize()
#     return res

# # task 4

# def number_to_string(num):
#    return str(num)

# # task 5

# def reverse(st):
#     words = st.split()
#     reversed_words = words[::-1]
#     return " ".join(reversed_words)

# task 6
def reverse_list(l):
    l.reverse()
    return l

# task 7
def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# task 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
  return fuel_left * mpg >= distance_to_pump

# task 9
def are_you_playing_banjo(name):
  if name.startswith('R') or name.startswith('r'):
    return name + ' plays banjo'
  return name + ' does not play banjo'

# task 10
def bool_to_word(boolean):
  return 'Yes' if boolean else 'No'

# task 11
def count_sheeps(sheep):
  return sheep.count(True)

# task 12
def correct_tail(body, tail):
  return body.endswith(tail)