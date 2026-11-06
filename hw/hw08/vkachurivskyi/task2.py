def validate_password(password):
    """Перевіряє валідність пароля за заданими критеріями"""
    if len(password) < 6 or len(password) > 16:
        return False
        
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    special_chars = "$#@"
    
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    if has_lowercase and has_uppercase and has_digit and has_special:
        return True
    return False

user_password = input("Введіть пароль для перевірки: ")

if validate_password(user_password):
    print("Пароль правильний")
else:
    print("Неправильний пароль")