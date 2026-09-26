import re

def validation_password(user_password : str) -> bool:

    """
    Validates a password against security complexity requirements.

    The password must be between 6 and 16 characters long and must contain
    at least one uppercase letter, one lowercase letter, one digit (1-9),
    and one special character from the set: $, #, @.

    Args:
        user_password (str): The password string to be validated.

    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    valid_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$"
    

    result = re.match(valid_pattern,user_password)
    return bool(result)
    



def main() -> None:
    while True:
        user_password = input("Input your password: ")
        if validation_password(user_password):
            print("Your password is valid")
            break
        else:
            print(
    "Your password is invalid\n"
    "It must contain at least 1 lowercase letter a-z\n"
    "It must contain at least 1 uppercase letter A-Z\n"
    "It must contain at least 1 number 0-9\n"
    "It must contain at least 1 special character $#@\n"
    "Total length must be between 6 and 16 characters"
)

if __name__ == "__main__" :
    main()