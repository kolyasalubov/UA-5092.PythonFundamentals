import re

password = input("Enter your password: ")

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"

if re.fullmatch(pattern, password):
    print("Password is valid.")
else:
    print("Invalid password.")