from task3_areas import rectangle_area, triangle_area, circle_area

def main() -> None:
    """
    Ask the user to choose a figure and display its area
    """
    print("1 - Прямокутник")
    print("2 - Трикутник")
    print("3 - Коло")

    choice = input("Оберіть фігуру (1-3): ")

    if choice not in ("1", "2", "3"):
        print("Неправильний вибір. Такого варіанту немає")
        return

    try:
        if choice == "1":
            a = float(input("Введіть сторону a: "))
            b = float(input("Введіть сторону b: "))

            if a <= 0 or b <= 0:
                print("Величини мають бути додатними")
                return

            area = rectangle_area(a, b)

        elif choice == "2":
            base = float(input("Введіть основу: "))
            height = float(input("Введіть висоту: "))

            if base <= 0 or height <= 0:
                print("Величини мають бути додатними")
                return

            area = triangle_area(base, height)

        else:
            radius = float(input("Введіть радіус: "))

            if radius <= 0:
                print("Радіус має бути додатним")
                return

            area = circle_area(radius)

    except ValueError:
        print("Потрібно ввести число")
        return

    print(f"Площа: {area:.2f}")


if __name__ == "__main__":
    main()