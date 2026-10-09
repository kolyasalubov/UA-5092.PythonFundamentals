import re
def validate_password(password: str) -> None:
    '''
    This function takes a password as input and checks if it meets the following criteria:
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character from the set [$#@]
    - Has a length between 6 and 16 characters (inclusive)
    If the password meets all the criteria, it prints "Valid password". Otherwise, it prints "Invalid password".

    Args:
        password (str): The password to be validated.
    '''

    pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}"

    if re.fullmatch(pattern, password):
        print("Valid password")
    else:
        print("Invalid password")


if __name__ == "__main__":
    password = input("Enter password: ")
    validate_password(password)


