def count_characters(text):
    """
    Function counts amount of each unique character and returns dictionary like {"a": 2}
    Args:
        text (str): Text input from user
    Returns:
        dict: Dictionary where key is character and value is count
    """
    characters_count = {}
    unique_character = list(dict.fromkeys(text))
    for character in unique_character:
        new_record = {character: text.count(character)}
        characters_count.update(new_record)
    return characters_count

if __name__ == "__main__":
    print(count_characters(input("Enter a word:\n> ")))

    