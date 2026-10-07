password = input('Enter password: ')

allowed_specials = '$#@'

if len(password) < 6 or len(password) > 16:
    print('Invalid: incorrect length')
else:
    has_lower = has_upper = has_digit = has_special = has_invalid = False

    for ch in password:
        if 'a' <= ch <= 'z':
            has_lower = True
        elif 'A' <= ch <= 'Z':
            has_upper = True
        elif '0' <= ch <= '9':
            has_digit = True
        elif ch in allowed_specials:
            has_special = True
        else:
            has_invalid = True
    if all([has_lower, has_upper, has_digit, has_special]) and not has_invalid:
        print('Valid password')
    else:
        print('Invalid password')
