import math

def rectangle_area(x: float, y: float) -> float:
    """сalculates the area of a rectangle"""
    if x <= 0 or y <= 0:
        raise ValueError("Сторони прямокутника мають бути додатними.")
    return x * y

def triangle_area(side_a: float, height: float) -> float:
    """сalculates the area of a triangle"""
    if side_a <= 0 or height <= 0:
        raise ValueError("Сторона та висота мають бути додатними.")
    return round(0.5 * side_a * height, 2)

def circle_area(r: float) -> float:
    """сalculates the area of a circle"""
    if r <= 0:
        raise ValueError("Радіус має бути додатним.")
    return round(math.pi * r**2, 2)

if __name__ == "__main__":
    print("Виберіть фігуру: \n 1 - Прямокутник \n 2 - Трикутник \n 3 - Коло")
    choose = int(input("Ваш вибір: "))

    if choose == 1:
        print(rectangle_area(float(input("Вкажіть першу сторону: ")), float(input("Вкажіть другу сторону: "))))
    elif choose == 2:
        print(triangle_area(float(input("Вкажіть довжину сторони: ")), float(input("Вкажіть висоту: "))))
    elif choose == 3:
        print(circle_area(float(input("Вкажіть радіус: "))))
    else:
        print("Неправильне число")