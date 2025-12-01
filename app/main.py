from string import ascii_lowercase


def check_password(password: str) -> bool:
    if len(password) not in range(8, 17):
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
            if letter.lower() not in ascii_lowercase:
                return False
        elif letter.isdigit():
            has_digit = True
        elif letter in "$@#&!-_":
            has_special = True
        else:
            return False
    return all([has_upper, has_digit, has_special])


try:
    print(check_password(None))
except Exception as e:
    print(e)
