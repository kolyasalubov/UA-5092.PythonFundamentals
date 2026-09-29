def password_check():
    import re

    password = input("Enter your password: ")

    if re.search(r"[$#@]", password) and re.search(r"[0-9]", password):
        if re.search(r"[a-z]", password) or re.search(r"[A-Z]", password):
            if 5 < len(password) < 17:
                return "Your password is correct."
            
    else:
        return "Your password is incorrect."

