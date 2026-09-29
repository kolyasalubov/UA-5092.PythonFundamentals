import areas


def get_positive_number(message: str) -> float:
    while True:
        number = input(message)

        if number.isdigit():
            number = float(number)

            if number > 0:
                return number
            else:
                print("The value must be greater than 0")
        else:
            print("Please enter a number")


if __name__ == "__main__":
    while True:
        choice = input("Choose rectangle, triangle or circle: ")

        if choice == "rectangle":
            a = get_positive_number("Enter a: ")
            b = get_positive_number("Enter b: ")    
            print(areas.rectangle(a, b))
            break

        elif choice == "triangle":
            a = get_positive_number("Enter a: ")
            h = get_positive_number("Enter h: ")
            print(areas.triangle(a, h))
            break

        elif choice == "circle":
            r = get_positive_number("Enter r: ")
            print(areas.circle(r))
            break

        else:
            print("Please choose rectangle, triangle or circle.")