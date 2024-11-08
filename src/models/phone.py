import re
from src.models.field import Field
from src.utils.validations import validate_phone

class Phone(Field):
    def __init__(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format. Use +380XXXXXXXXX")
        super().__init__(phone)

    @staticmethod
    def validate_phone(phone):
        return validate_phone(phone)