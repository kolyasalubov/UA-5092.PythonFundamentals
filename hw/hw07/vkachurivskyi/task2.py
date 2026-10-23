import math

def rectangle_area(x, y):
    """Обчислює площу прямокутника"""
    return x * y

def triangle_area(side_a, height):
    """Обчислює площу трикутника"""
    return 0.5 * side_a * height

def circle_area(r):
    """Обчислює площу кола"""
    return math.pi * r**2

print("Виберіть фігуру: \n 1 - Прямокутник \n 2 - Трикутник \n 3 - Коло")
choose = int(input("Ваш вибір: "))

if choose == 1:
    num_x = float(input("Вкажіть першу сторону: "))
    num_y = float(input("Вкажіть другу сторону: "))
    result = rectangle_area(num_x, num_y)
    print(f"Площа прямокутника: {result}")
    
elif choose == 2:
    num_side = float(input("Вкажіть довжину сторони: "))
    num_height = float(input("Вкажіть висоту: "))
    result = triangle_area(num_side, num_height)
    print(f"Площа трикутника: {result:.2f}")
    
elif choose == 3:
    num_r = float(input("Вкажіть радіус: "))
    result = circle_area(num_r)
    print(f"Площа кола: {result:.2f}")
    
else:
    print("Неправильне число")
