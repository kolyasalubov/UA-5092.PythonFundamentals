def person_age():
    age = input("Enter age: ")
    try:
        age = int(age)
    except (ValueError, TypeError):
        return "You entered not a number."

        
    if age >= 0:
        if age % 2 == 0:
            return f"You are {age} years old. And your age is even."
        else:
            return f"You are {age} years old. And your age is odd."
    raise ValueError ("You enter negative number")

print(person_age())