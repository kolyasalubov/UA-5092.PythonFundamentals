# 1. Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# 2. Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    
    x_difference = x2 - x1
    y_difference = y2 - y1
    distance_result = (x_difference ** 2 + y_difference ** 2) ** 0.5
    return round(distance_result, 2)

print(distance(4, 6, 7, 9))
    
# 3. No yelling!

def filter_words(st):
    st = " ".join(st.split())
    return st.capitalize()

# 4. Convert a Number to a String

def number_to_string(num):
    a = str(num)
    return a

# 5. Reversing Words in a String

def reverse(st):
    words = st.split()
     
    return " ".join(words)

# 6. Reverse List Order

def reverse_list(l):
    return l[::-1]

# 7. Multiples of 3 or 5

def solution(number):
    if number < 0:
        return 0

    total = 0

    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total += num

    return total

# 8. Will you make it?

def zero_fuel(distance, mpg, fuel_left):
    if mpg * fuel_left >= distance:
        return True
    else:
        return False
    
# 9. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# 10. Convert boolean values to strings 'Yes' or 'No'

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
# 11. Counting sheep

def count_sheeps(sheep):
    count = 0

    for item in sheep:
        if item == True:
            count += 1

    return count

# 12. Is this my tail?

def correct_tail(body, tail):
    sub = body[-len(tail):]

    if sub == tail:
        return True
    else:
        return False