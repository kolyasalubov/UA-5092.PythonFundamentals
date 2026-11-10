import math




def area_of_rectangle(length, width):
    return length * width


def area_of_triangle(side, height):
    return side / 2 * height


def area_of_circle(radius):
    return math.pi * (radius ** 2)

print('Hello!, choose the figure')
print("1 - Rectangle")
print('2 - Triangle')
print('3 - Circle')

choise = input('Enter your choise:')

if choise == '1':
    length = float(input('Whats the lenght?'))
    width = float(input('Whats the width?'))
    print('The are of rectangle:', area_of_rectangle(length, width))
elif choise == '2':
    side = float(input('Whats the side?'))
    height = float(input('Whats the height?'))
    print('The are of triangle:', area_of_triangle(side, height))
elif choise == '3':
    radius = float(input('Whats the radius?'))
    print('The area of circle:', area_of_circle(radius))
else:
    print('Invalid choise!')
