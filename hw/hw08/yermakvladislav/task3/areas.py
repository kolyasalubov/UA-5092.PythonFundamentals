import math

def area_rectangle():
  
  a = int(input("Side a: "))
  b = int(input("Side b: "))
  
  S = a * b
  
  return S

def area_triangle():
  a = int(input("Side a: "))
  h = int(input("Height: "))
  
  S = 0.5 * h * a
  
  return S

def area_circle():
  r = int(input("Radius: "))
  
  S = math.pi * pow(r, 2)
  S = round(S, 2)
  
  return S
  