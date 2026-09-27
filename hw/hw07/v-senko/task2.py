def area_rectangle(width, height):
    return width * height
 
def area_triangle(base, height):
    return 0.5 * base * height
 
def area_circle(radius):
    return math.pi * radius ** 2
 

def run_area_calculator():
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
 
    choice = input("Enter your choice (1/2/3): ").strip()
 
    if choice == "1":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(f"Area of rectangle: {area_rectangle(width, height)}")
 
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of triangle: {area_triangle(base, height)}")
 
    elif choice == "3":
        radius = float(input("Enter radius: "))
        print(f"Area of circle: {area_circle(radius)}")
 
    else:
        print("Invalid choice.")
