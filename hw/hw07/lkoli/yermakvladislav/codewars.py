"""
task1
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
"""

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
     
print(greet("James"))


"""
task2
Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.
"""

def distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    distance = round(distance, 2)
    return distance
  
print(distance(1, 1, 0, 0))


"""
task3
Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. String should be capitalized and properly spaced.
"""

def filter_words(st):
    st = st.lower()
    st = st.capitalize()
    st = " ".join(st.split())
    return st

print(filter_words('HELLO world!'))
      

"""
task4
We need a function that can transform a number (integer) into a string.
"""

def number_to_string(num):
    result = str(num)
    return result
  
print(number_to_string(67))


"""
task5
You need to write a function that reverses the words in a given string. Words are always separated by a single space.
"""

def reverse(st):
    st = st.split(" ")
    result = f"{st[1]} {st[0]}"
    return result
  
print(reverse('Hello World'))


"""
task6
In this kata you will create a function that takes in a list and returns a list with the reverse order.
"""

def reverse_list(l):
    l = l[::-1]
    return l
  
print(reverse_list([1,2,3,4]))


"""
task7
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
"""

def solution(number):
    result = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    
    return result
  
print(solution(16))


"""
task8 
You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.
"""

def zero_fuel(distance_to_pump, mpg, fuel_left):
    miles = mpg * fuel_left
    if distance_to_pump > miles:
        return False
    else:
        return True
      
print(zero_fuel(50, 25, 2))


"""
task9
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
"""

def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        result = f"{name} plays banjo"
        return result
    else:
        result = f"{name} does not play banjo"
        return result
      
print(are_you_playing_banjo("martin"))


"""
task10
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"
  
print(bool_to_word(True))


"""
task11
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
"""

def count_sheeps(sheep):
    quantity = 0
    for s in sheep:
        if s:
            quantity += 1
    
    return quantity
  

"""
task12
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
"""

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
      
print(correct_tail("Fox", "x"))
