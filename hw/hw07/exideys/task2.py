PI = 3.14

def area_rectangle(height : float,width: float) -> float:
    """
    Find the area of a rectangle
    input : height : float, width : float
    return : area of reactangle : float
    """
    return height * width

def area_triangle(base : float,height : float) -> float:
    """
    Find the area of a triangle
    input : base : float, height : float
    return : area of triangle : float
    """

    return 0.5 * base * height

def area_circle(radius : float ) -> float:
    """
    Find the area of a circle
    input : radius : float
    return : area of triangle : float
    """
    return PI * radius**2

def main():
    """
    Display the menu and call the selected area function
    input : user option and shape parameters
    """
    while True:
        print("1. Area of rectangle:")
        print("2. Area of triangle:")
        print("3. Area of circle:")
        user_option = (input("Input your option: "))
        match user_option:
            case "1":
                height = float(input("Input height"))
                width = float(input("Input width"))
                print("The area of rectangle is :",area_rectangle(height,width))
            case "2":
                base = float(input("Input base"))
                height = float(input("Input height"))
                print("The area of triangle is :",area_triangle(base,height))
            case "3" :
                radius = float(input("Input radius"))
                print("The area of circle is :",area_circle(radius))
            case _:
                print("Invalid option try again")
            
main()