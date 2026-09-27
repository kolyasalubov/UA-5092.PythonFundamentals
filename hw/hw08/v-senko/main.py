import area_calculator

def run_area_calculator():
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
 
    choice = input("Enter your choice (1/2/3): ").strip()
 
    if choice == "1":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(f"Area of rectangle: {area_calculator.area_rectangle(width, height)}")
 
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of triangle: {area_calculator.area_triangle(base, height)}")
 
    elif choice == "3":
        radius = float(input("Enter radius: "))
        print(f"Area of circle: {area_calculator.area_circle(radius)}")
 
    else:
        print("Invalid choice.")


if __name__ == "__main__": 
    run_area_calculator()
