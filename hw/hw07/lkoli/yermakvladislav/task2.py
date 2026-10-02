def calculation_of_area():


  figure = input("Choose figure: Rectangle, Triangle, Circle ")
  figure = figure.lower()


  if figure == "rectangle":
    a = int(input("Side A "))
    b = int(input("Side B "))
    s = a * b
    return s
  elif figure == "triangle":
    a = int(input("Side A "))
    b = int(input("Side B "))
    c = int(input("Side С "))
    
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s
    
  else:
    r = int(input("Radius "))
    s = 3.14159 * r ** 2
    return s
    
print(calculation_of_area())
