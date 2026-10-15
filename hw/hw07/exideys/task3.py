user_input = input("Input string: ")


def calculate_number_characters(user_input: str) -> dict:
    """
    Calculate numbers in characters
    input : user_input : str
    return : dict{letter : counter of number}
    """
    characters = {}
    for i in user_input:
        counter = user_input.count(i)
        characters[i] = counter
    return characters
