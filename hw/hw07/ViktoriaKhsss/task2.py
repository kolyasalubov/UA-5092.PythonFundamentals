def rectangle_area(a: float, b: float) -> float:
    """
    Returns the area of a rectangle
    """
    S = a * b
    return S


def triangle_area(a: float, h: float) -> float:
    """
    Returns the area of a triangle
    """
    S = (a * h) / 2
    return S


def circle_area(r: float) -> float:
    """
    Returns the area of a circle
    """
    S = 3.14 * r * r
    return S


choice = input("Choose rectangle, triangle or circle: ")

if choice == "rectangle":
    a = input("Enter a: ")

    while not a.isdigit():
        print("Please enter a number")
        a = input("Enter a: ")

    a = int(a)

    b = input("Enter b: ")

    while not b.isdigit():
        print("Please enter a number")
        b = input("Enter b: ")

    b = int(b)

    print(rectangle_area(a, b))

elif choice == "triangle":
    a = input("Enter a: ")

    while not a.isdigit():
        print("Please enter a number")
        a = input("Enter a: ")

    a = int(a)

    h = input("Enter h: ")

    while not h.isdigit():
        print("Please enter a number")
        h = input("Enter h: ")

    h = int(h)

    print(triangle_area(a, h))

elif choice == "circle":
    r = input("Enter r: ")

    while not r.isdigit():
        print("Please enter a number")
        r = input("Enter r: ")

    r = int(r)

    print(circle_area(r))

else:
    print("Please choose again")