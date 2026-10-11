def process_age(age_input):
    """
    Обробляє введений вік, перевіряє, що він не є від’ємним,
    та повертає інформацію, чи є він парним або непарним.
    """

    age = int(age_input)
    
    if age < 0:
        raise ValueError("Age cannot be a negative number!")
        
    if age % 2 == 0:
        return f"The age {age} is Even."
    else:
        return f"The age {age} is Odd."

if __name__ == "__main__":
    user_input = input("Enter your age: ")
    
    try:
        result = process_age(user_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


