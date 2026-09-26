def count_characters(input_str: str = "hello") -> dict:
    """
    Обчислює кількість входжень кожного символу в заданому рядку.
    Повертає: dict
    """
    result = {}

    for character in input_str:
        result[character] = result.get(character, 0) + 1

    return result
