import areas

choice = input("Choose rectangle, triangle or circle: ")

if choice == "rectangle":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print(areas.rectangle(a, b))

elif choice == "triangle":
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    print(areas.triangle(a, h))

elif choice == "circle":
    r = float(input("Enter r: "))
    print(areas.circle(r))

else:
    print("Please choose rectangle, triangle or circle")