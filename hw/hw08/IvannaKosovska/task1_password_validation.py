import re

def is_valid_password(password_text: str) -> str:
    has_lower = bool(re.search(r"[a-z]", password_text))
    has_upper = bool(re.search(r"[A-Z]", password_text))
    has_digit = bool(re.search(r"[0-9]", password_text))
    has_special = bool(re.search(r"[$#@]", password_text))
    valid_length = 6 <= len(password_text) <= 16
    return has_lower and has_upper and has_digit and has_special and valid_length


password_entered = input("Your password: ")

if is_valid_password(password_entered):
    print("Your password is valid")
else:
    print("Your password is invalid")