def rectangle_area(a, b):
  """
  Returns the area of a rectangle
  """
  S = a * b
  return S

def triangle_area(a, h):
  """
  Returns the area of a triangle
  """
  S = (a * h) / 2
  return S

def circle_area(r):
  """
  Returns the area of a circle
  """
  S = 3.14 * r * r
  return S


choice = input("Choose rectangle, triangle or circle: ")

if choice == "rectangle":
  a = int(input("Enter a: "))
  b = int(input("Enter b: "))
  print(rectangle_area(a , b))

elif choice == "triangle":
  a = int(input("Enter a: "))
  h = int(input("Enter h: "))
  print(triangle_area(a , h))

elif choice == "circle":
 r = int(input("Enter r: "))
 print(circle_area(r))

else:
  print("Please choose again")

