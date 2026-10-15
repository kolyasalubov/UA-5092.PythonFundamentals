'''
Module that implements function of validating password with following requirements:
    At least 1 lowercase letter in range [a-z] and 1 uppercase letter in range [A-Z].
    At least 1 digit in the range [0-9].
    At least 1 character from the set [$#@].
    Minimum length: 6 characters.
    Maximum length: 16 characters.
'''

import re

PATTERN = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$")

def validate_password(password: str) -> bool:
    '''
    The function that validates password 
        Args:
            password: user password
        Returns:
            True: when password matches requirements
            False: when password doesn`t match requirements
    '''
    return re.fullmatch(PATTERN, password)

if __name__ == "__main__":
    while True:
        user_password = input("Please enter your password:\n")
        
        if validate_password(user_password):
            print("Your password is valid. Access.")
            break
        else:
            print("Your password doesn`t match the requirements. Try again.\n")
