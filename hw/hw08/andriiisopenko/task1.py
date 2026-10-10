
def check_password(password):
    """Check if the password meets all requirements."""
    if not 6 <= len(password) <= 16:
        return False
    has_lower = any('a' <= char <= 'z' for char in password)
    has_upper = any('A' <= char <= 'Z' for char in password)
    has_digit = any('0' <= char <= '9' for char in password)
    has_special = any(char in '$#@' for char in password)
    return has_lower and has_upper and has_digit and has_special

print("Password requirements:")
print("- Length: 6-16 characters")
print("- At least 1 lowercase letter (a-z)")
print("- At least 1 uppercase letter (A-Z)")
print("- At least 1 digit (0-9)")
print("- At least 1 special character ($, #, @)")
password = input("\nEnter your password: ")

if check_password(password):
    print("Valid password")
else:
    print("Invalid password")