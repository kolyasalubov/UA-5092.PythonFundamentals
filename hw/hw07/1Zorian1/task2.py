import math

def triangle_area(a , h):
      return 0.5 * a * h

def rectangle_area(a , b):
      return a * b

def circle_area(r):
      return math.pi * (r ** 2)


figure_choose = input("choose your figure: triangle , rectangle , circle: \n ")
figure_list = ['triangle', 'rectangle', 'circle']
if figure_choose == 'triangle':
    a = float(input("Enter your base: "))
    h = float(input("Enter your height: "))
    result = triangle_area(a , h)
    print(f"triangle area:{result}")
elif figure_choose == 'rectangle':
      a = float(input("Enter side a: "))
      b = float(input("Enter side b: "))
      result = rectangle_area(a , b )
      print(f"Rectangle area: {result}")
elif figure_choose == "circle":
      r = float(input("Enter circle radius: "))
      result = circle_area(r)
      print(f"Your circle area: {result}")
else :
      print("Choose figure only provided in list!")
