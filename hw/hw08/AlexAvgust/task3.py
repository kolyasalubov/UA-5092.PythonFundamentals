import calculate_area

def main():
    '''
    This function provides a menu for the user to choose a geometric figure (rectangle, triangle, or circle) and calculates the area based on user input.
    It prompts the user for the necessary dimensions and displays the calculated area.
    '''
    print("Choose a figure:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    choice = input("Enter your choice: ")

    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        result = calculate_area.area_of_rectangle(length, width)
        print(f"Area: {result}")

    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))

        result = calculate_area.area_of_triangle(base, height)
        print(f"Area: {result}")

    elif choice == "3":
        radius = float(input("Enter radius: "))

        result = calculate_area.area_of_circle(radius)
        print(f"Area: {result}")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()