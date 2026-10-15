from math import pi, pow
import areas

print("Виберіть фігуру для обчислення площі:")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Коло")

choice = input("Введіть номер: ")

if choice == '1':
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    print(f"Площа прямокутника: {areas.rectangle_area(a, b)}")
    
elif choice == '2':
    a = float(input("Введіть основу a: "))
    h = float(input("Введіть висоту h: "))
    print(f"Площа трикутника: {areas.triangle_area(a, h)}")
    
elif choice == '3':
    r = float(input("Введіть радіус r: "))
    print(f"Площа кола: {areas.circle_area(r)}")
    
else:
    print("Невірний вибір.")