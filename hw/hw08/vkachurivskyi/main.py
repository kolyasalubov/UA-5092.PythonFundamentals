import areas

print("Виберіть фігуру: \n 1 - Прямокутник \n 2 - Трикутник \n 3 - Коло")
choose = int(input("Ваш вибір: "))

if choose == 1:
    num_a = float(input("Вкажіть першу сторону: "))
    num_b = float(input("Вкажіть другу сторону: "))
    result = areas.rectangle_area(num_a, num_b)
    print(f"Площа прямокутника: {result}")
    
elif choose == 2:
    num_h = float(input("Вкажіть висоту: "))
    num_a = float(input("Вкажіть сторону: "))
    result = areas.triangle_area(num_h, num_a)
    print(f"Площа трикутника: {result:.2f}")
    
elif choose == 3:
    num_r = float(input("Вкажіть радіус: "))
    result = areas.circle_area(num_r)
    print(f"Площа кола: {result:.2f}")
    
else:
    print("Неправильне число")
