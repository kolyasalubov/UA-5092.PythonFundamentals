import math

#1
def greet(name):
    """
    Special greeting for Johny
    """
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
#2
def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Function to find distance between two points
    """
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)
#3
def filter_words(st):
    """
    Function to remove multiple spaces and make words normal, not in uppercase
    """
    
    words = list(filter(lambda word: word, st.split(" ")))
    words = list(map(lambda word: word.lower(), words))
    resulting_text = " ".join(words).capitalize()
    
    return resulting_text
#4
def number_to_string(num: int) -> str:
    """
    Funciton to convert number to string
    """
    
    try:
        result = str(num)
    except ValueError as e:
        print(e)
        return None
    else:
        return result
#5
def reverse(st):
    """
    Funciton to reverse words order in a string
    """
    return " ".join(st.split(" ")[::-1])
#6
def reverse_list(l):
    """Function to return a list with the reverse order of l"""
    return l[::-1]
#7
def solution(number: int) -> int:
    """
    Function to find sum of all numbers which are multipes of 3 or 5 and less then number
    Args:
        number (int): number below which we will find multiples of 3 and 5
    Returns:
        int: sum of all numbers which are multiples of 3 or 5
    """
    if number <= 0:
        return 0
    sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum
#8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    Function to define if it's possible to reach pump
    """
    return True if distance_to_pump - mpg * fuel_left <= 0 else False
#9
def are_you_playing_banjo(name):
    """
    Function to aswer qustion Are you playing banjo?
    """
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"
#10
def bool_to_word(boolean):
    """
    Function to convert boolean value to string Yes or Nool
    """
    return "Yes" if boolean else "No"
#11
def count_sheeps(sheeps):
    """
    Funciton to count sheeps
    """
    if sheeps:
        return sheeps.count(True)
    return 0
#12
def correct_tail(body, tail):
    """
    Funciton to check if tail fits, last letter should be equal to tail
    """
    return True if body[-1] == tail else False