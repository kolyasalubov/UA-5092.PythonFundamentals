def largest(a, b):
    """Повертає найбільше число"""
    if a > b:
        return a
    return b

num_a = float(input("Введіть число a: "))
num_b = float(input("Введіть число b: "))

result = largest(num_a, num_b)
print(f"Найбільше число: {result}")
