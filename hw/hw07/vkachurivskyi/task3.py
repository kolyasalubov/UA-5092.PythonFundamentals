def count_characters(text):
    """Обчислює кількість входжень кожного символу в рядку"""
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

input_text = input("Введіть будь-який текст: ")

result = count_characters(input_text)
print(f"Результат підрахунку символів: {result}")
