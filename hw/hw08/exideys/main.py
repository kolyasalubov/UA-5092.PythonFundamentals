import area_shapes as area


def main() -> None:
    while True:
        print("1.Area of rectangle: ")
        print("2.Area of triangle: ")
        print("3.Area of circle: ")

        try:
            user_input = int(input("Input your's option: "))
        except ValueError:
            print("Value Error")
    
        match user_input:
            case 1:
                width = float(input("Input width: "))
                height = float(input("Input height: "))
                print(f"Area of rectangle is :  {area.area_rectangle(width,height)}")
                break
            case 2:
                height = float(input("Input height: "))
                base = float(input("Input base: "))
                print(f"Area of triangle is : {area.area_triangle(height,base)}")
                break
            case 3:
                radius = float(input("Input radius: "))
                print(f"Area of circle is : {area.area_circle(radius)}")
                break
            case _ :
                print("Invalid option")
            

if __name__ == "__main__":
    main()

