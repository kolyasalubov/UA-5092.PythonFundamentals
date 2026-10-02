import area_calculator_Ivanna

user_choice = input("Please select the figure whose area you'd like to calculate: rectangle, triangle, or circle: ").lower()

while user_choice != "rectangle" and user_choice != "triangle" and user_choice != "circle":
    user_choice = input("Sorry, unknown figure entered." \
                       " Please select the figure whose area you'd like to calculate: rectangle, triangle, or circle: ").lower()

if user_choice == "rectangle":
    length = float(input("Please enter the length: "))
    width = float(input("Please enter the width: "))
    print(round(area_calculator_Ivanna.rectangle_area(length, width), 2))

elif user_choice == "triangle":
    height = float(input("Please enter the height: "))
    base = float(input("Please enter the base: "))
    print(round(area_calculator_Ivanna.triangle_area(base, height), 2))

else:
    radius = float(input("Please enter the radius: "))
    print(round(area_calculator_Ivanna.circle_area(radius), 2))