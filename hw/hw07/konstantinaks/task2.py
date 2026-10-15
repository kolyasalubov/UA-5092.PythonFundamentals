import math

def area_rectangle(a, b):
    """
    Обчислює площу прямокутника за двома сторонами
    """
    return a * b

def area_triangle(a, h):
    """
    Обчислює площу трикутника за основою та висотою
    """
    return 0.5 * a * h

def area_circle(r):
    """
    Обчислює площу кола за радіусом
    """
    return math.pi * (r ** 2)

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    
    choice = input("Введіть номер фігури (1-3): ")

    if choice == "1":
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        res = area_rectangle(a, b)
        print(f"Площа прямокутника: {res}")
        
    elif choice == "2":
        a = float(input("Введіть основу a: "))
        h = float(input("Введіть висоту h: "))
        res = area_triangle(a, h)
        print(f"Площа трикутника: {res}")
        
    elif choice == "3":
        r = float(input("Введіть радіус r: "))
        res = area_circle(r)
        print(f"Площа кола: {res:.2f}")
        
    else:
        print("Невірний вибір фігури!")

# Запуск програми
main()
