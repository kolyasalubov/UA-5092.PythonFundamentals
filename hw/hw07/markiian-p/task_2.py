import math

def rectangle_area(x: float, y: float):
    area = x * y
    return area

def triangle_area(side_a: float, height: float):
    area = round(0.5 * side_a * height, 2)
    return area

def circle_area(r: float):
    # Використовуємо math.pi напряму
    area = round(math.pi * r**2, 2) 
    return area

if __name__ == "__main__":
    print("Виберіть фігуру: \n 1 - Прямокутник \n 2 - Трикутник \n 3 - Коло")
    choose = int(input("Ваш вибір: "))

    if choose == 1:
        # Уважно стежимо за дужками!
        print(rectangle_area(float(input("Вкажіть першу сторону: ")), float(input("Вкажіть другу сторону: "))))
    elif choose == 2:
        print(triangle_area(float(input("Вкажіть довжину сторони: ")), float(input("Вкажіть висоту: "))))
    elif choose == 3:
        print(circle_area(float(input("Вкажіть радіус: "))))
    else:
        print("Неправильне число")