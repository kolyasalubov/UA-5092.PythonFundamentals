# hw 07(2)Codewars

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

# 2

# import math
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
    
#     d = math.sqrt(dx**2 + dy**2)
    
#     return round(d, 2)

# print(distance(1,1,4,5))


# 3

# import random

# color_list = [ 'red' , 'blue', 'green']

# print(random.choice(color_list))

# \\\\\\\\\\\\\\\\\\\\\\\\\

# def filter_words(st):
#     words = st.split()
#     return " ".join(words).capitalize()

# 4

# def number_to_string(num):
#     return  str(num)

# 5

# def reverse(st):    
#     return " ".join(st.split()[::-1])

# 6

# def reverse_list(l):
#     'return a list with the reverse order of l'
#     return l[::-1]

# def solution(number):
#     if number < 0:
#         return 0
#     total = 0
#     for x in range(number):
#         if x % 3 == 0 or x % 5 == 0:
#             total += x  
#     return total

# 7

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump / fuel_left == mpg:
#         return True
#     else:
#         return False

# 8
# def are_you_playing_banjo(name):
#     if name[0] == "R" or name[0] == "r":
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"

# 9

# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"

# 10

# def count_sheeps(sheep):
#     count = 0
#     for item in sheep:
#         if item == True:  
#             count += 1
#     return count

# 11

# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     else:
#         return False