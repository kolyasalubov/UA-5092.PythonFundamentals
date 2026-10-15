import re

def check_password(password: str) -> bool:
    """
    Checks the validity of a password based on specific criteria.

    Args:
        password (str): The password string to be validated.

    Returns:
        bool: True if the password meets all validation criteria, False otherwise.
    """
    validity_condition = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[a-zA-Z0-9$#@]{6,16}$"
    return bool(re.match(validity_condition, password))

password = input("Enter your password please: ")
status = "valid" if check_password(password) else "invalid"
print(f"Your password is {status}!")