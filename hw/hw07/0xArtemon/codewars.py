# 1. Jenny's secret message
def greet(name):
    return f"Hello, {'my love' if name == 'Johnny' else name}!"

# 2. Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)

# 3. No yelling!
def filter_words(st):
    return " ".join(st.capitalize().split())

# 4. Convert a Number to a String!
def number_to_string(num):
    return str(num)

# 5. Reversing Words in a String
def reverse(st):
    return ' '.join(st.split()[::-1])

# 6. Reverse List Order
def reverse_list(l):
    return l[::-1]

# 7. Multiples of 3 or 5
def solution(number):
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)

# 8. Will you make it?
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# 9. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"

# 10. Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# 11. Counting sheep...
def count_sheeps(sheep):
    return sum(x for x in sheep if x)

# 12. Is this my tail?
def correct_tail(body, tail):
    return tail == body[-1]
