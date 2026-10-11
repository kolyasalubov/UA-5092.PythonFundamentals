import areas

print("Choose a figure:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")
choice = input("Enter your choice (1-3): ")

if choice == "1":
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    if a > 0 and b > 0:
        print("Rectangle area:", areas.rectangle_area(a, b))
    else:
        print("Dimensions must be positive.")
elif choice == "2":
    h = float(input("Enter height: "))
    a = float(input("Enter base: "))
    if h > 0 and a > 0:
        print("Triangle area:", areas.triangle_area(h, a))
    else:
        print("Dimensions must be positive.")
elif choice == "3":
    r = float(input("Enter radius: "))
    if r > 0:
        print("Circle area:", areas.circle_area(r))
    else:
        print("Radius must be positive.")
else:
    print("Invalid choice.")