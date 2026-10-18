def process_age(age):
    if age < 0:
        raise ValueError("age cannot be a negative number.")
    
    if age % 2 == 0:
        return "the entered age is even."
    else:
        return "the entered age is odd."

try:
    user_input = int(input("enter your age: "))
    result = process_age(user_input)
    print(result)
except ValueError as e:
    print(f"error: {e}")