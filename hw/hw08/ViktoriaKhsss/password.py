import re

def validate_password(password: str) -> bool:
    """
    Checks if the password is valid.
    """
    if len(password) < 6 or len(password) > 16:
        print("Enter a password from 6 to 16 characters")
        return False

    if not re.search("[a-z]", password):
        print("Password must contain a lowercase letter")
        return False

    if not re.search("[A-Z]", password):
        print("Password must contain an uppercase letter")
        return False

    if not re.search("[0-9]", password):
        print("Password must contain a number")
        return False

    if not re.search("[$#@]", password):
        print("Password must contain $, # or @")
        return False

    print("Password is correct")
    return True


password = input("Enter your password: ")

print(validate_password(password))