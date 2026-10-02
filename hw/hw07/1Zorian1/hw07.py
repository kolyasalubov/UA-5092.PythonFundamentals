#Taks 1

# def higher_number(num1, num2):
#     """
#     returns the largest number of numbers
    
#     """
#     if num1 > num2:
#         return num1
#     else :
#         return num2

# first_number = float(input("Enter your first number:"))
# second_number = float(input("Enter your second number:"))

# result = higher_number(first_number, second_number)
# print(result)

#Task2
# import math

# def triangle_area(a , h):
#       return 0.5 * a * h

# def rectangle_area(a , b):
#       return a * b

# def circle_area(r):
#       return math.pi * (r ** 2)


# figure_choose = input("choose your figure: triangle , rectangle , circle: \n ")
# figure_list = ['triangle', 'rectangle', 'circle']
# if figure_choose == 'triangle':
#     a = float(input("Enter your base: "))
#     h = float(input("Enter your height: "))
#     result = triangle_area(a , h)
#     print(f"triangle area:{result}")
# elif figure_choose == 'rectangle':
#       a = float(input("Enter side a: "))
#       b = float(input("Enter side b: "))
#       result = rectangle_area(a , b )
#       print(f"Rectangle area: {result}")
# elif figure_choose == "circle":
#       r = float(input("Enter circle radius: "))
#       result = circle_area(r)
#       print(f"Your circle area: {result}")
# else :
#       print("Choose figure only provided in list!")


#Task 3

# def word_calculator(word):
#     result_dict = {}

#     for letter in word:
#         if  letter in result_dict:
#             result_dict[letter] += 1
#         else : 
#             result_dict[letter] = 1
#     return result_dict

# user_word = input("Enter a word: ")
# print(word_calculator(user_word))


# hw 07(2)Codewars
name = input("Enter: ")

def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
    
