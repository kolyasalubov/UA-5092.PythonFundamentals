import area_calculation as ar_calc

def calculate_area():
    '''
    The program's entry point. Displays a menu to the user and calls the 
    appropriate functions for calculating areas.
    '''
    while True:
        print(f"{'-' * 30} Areas menu {'-' * 30}")
        print("1. Calculate rectangle area")
        print("2. Calculate triangle area")
        print("3. Calculate circle area")
        print("4. Quit")
    
        user_input = input("\nChoose your option: ")
    
        match user_input:
            case "1":
                length = ar_calc.check_number("Enter length: ")
                width = ar_calc.check_number("Enter width: ")
                print(f"Area of your rectangle is: {ar_calc.rectangle_area(length, width)}\n")
            case "2":
                base = ar_calc.check_number("Enter base: ")
                height = ar_calc.check_number("Enter height: ")
                print(f"Area of your triangle is: {ar_calc.triangle_area(base, height)}\n")
            case "3":
                radius = ar_calc.check_number("Enter radius: ")
                print(f"Area of your circle is: {ar_calc.circle_area(radius)}\n")
                print("Please enter a valid number.\n")
            case "4":
                break
            case _:
                print("Invalid input. Try again\n")

if __name__ == "__main__":
    calculate_area()