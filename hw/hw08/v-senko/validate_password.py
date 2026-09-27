import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    return re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).*$', password)

if __name__ == "__main__":
    user_password = input("Enter a password to validate: ")

    print("Valid password." if validate_password(user_password) else "Invalid password. Please ensure it meets the criteria.")
