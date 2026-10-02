import math

def rectangle_area(a, b):
    """Обчислює площу прямокутника."""
    if a <= 0 or b <= 0:
        return None
    return a * b


def triangle_area(a, h):
    """Обчислює площу трикутника."""
    if a <= 0 or h <= 0:
        return None
    return (a * h) / 2


def circle_area(r):
    """Обчислює площу круга."""
    if r <= 0:
        return None
    return math.pi * r ** 2


def show_result(name, area):
    """Виводить результат обчислення."""
    if area is None:
        print("Помилка! Значення повинні бути більшими за нуль.")
    else:
        print(f"Площа фігури ({name}): {area:.2f}")


def main():
    print("=== Обчислення площі фігур ===")
    print("1 - Прямокутник")
    print("2 - Трикутник")
    print("3 - Круг")

    choice = input("Оберіть номер фігури: ")

    if choice == "1":
        a = float(input("Введіть довжину першої сторони: "))
        b = float(input("Введіть довжину другої сторони: "))

        result = rectangle_area(a, b)
        show_result("прямокутник", result)

    elif choice == "2":
        a = float(input("Введіть довжину основи: "))
        h = float(input("Введіть висоту трикутника: "))

        result = triangle_area(a, h)
        show_result("трикутник", result)

    elif choice == "3":
        r = float(input("Введіть радіус круга: "))

        result = circle_area(r)
        show_result("круг", result)

    else:
        print("Такого пункту меню немає. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
    