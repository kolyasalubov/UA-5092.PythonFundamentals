import math
"""
This 3 functions calculate area of different figure, 1 - rectangle, 
2 - triangle, 3 - circle
"""

def rectangle_area(widt, height):
    return widt * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * (radius ** 2)

print("Choise the option for calculate area: 1 - rectangle, 2 - triangle, 3 - circle")

choice = input('enter: ')

if choice == '1':
    w = float(input('Enter width: '))
    h = float(input('enter height: '))
    print('rectangle area:', rectangle_area(w, h))

elif choice == '2':
    b = float(input('Enter base: '))
    h = float(input('enter height '))
    print('triangle area:', triangle_area(b, h))

elif choice == '3':
    r = float(input('Enter radius: '))
    print('circle area:', circle_area(r))

else:
    print('gg')
