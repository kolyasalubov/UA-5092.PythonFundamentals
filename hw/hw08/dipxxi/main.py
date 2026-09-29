# Імпортуємо створений модуль з геометричними функціями
import geometry


def main():
    print("Площу якої фігури ви хочете обчислити?")
    print("1 — Прямокутник")
    print("2 — Трикутник")
    print("3 — Круг")

    choice = input("Введіть номер (1-3): ").strip()

    if choice == "1":
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        area = geometry.rectangle_area(a, b)
        print(f"Площа прямокутника: {area}")

    elif choice == "2":
        h = float(input("Введіть висоту h: "))
        a = float(input("Введіть основу a: "))
        area = geometry.triangle_area(h, a)
        print(f"Площа трикутника: {area}")

    elif choice == "3":
        r = float(input("Введіть радіус r: "))
        area = geometry.circle_area(r)
        print(f"Площа круга: {area}")

    else:
        print("Неправильний вибір. Будь ласка, запустіть програму знову.")


if __name__ == "__main__":
    main()

