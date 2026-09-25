# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

# No yelling!
def filter_words(st):
    return " ".join(word for word in st.split(" ") if word != "").capitalize()

# Convert a Number to a String
def number_to_string(num):
    return str(num)

# Reversing Words in a String
def reverse(st):
    return ' '.join(reversed(st.split(' ')))

# Reverse List Order
def reverse_list(l):
    return l[::-1]

# Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    counter = 1
    summ = 0
    while counter < number:
        if not counter % 3 or not counter % 5:
            print(counter)
            summ += counter
        counter += 1
    return summ

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == 'r' else f"{name} does not play banjo"

# Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Counting sheep
def count_sheeps(sheeps):
    return sum(1 for sheep in sheeps if bool(sheep))

# Is this my tail?
def correct_tail(body, tail):
    return body[-1:] == tail