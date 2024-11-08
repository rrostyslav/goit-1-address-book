import re

def validate_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))
    # return True

def validate_phone(phone):
    return bool(re.match(r'^\+380\d{9}$', phone))
    # return True