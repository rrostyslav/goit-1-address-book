import re
from src.models.field import Field
from src.utils.validations import validate_email

class Email(Field):
    def __init__(self, email):
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        super().__init__(email)

    @staticmethod
    def validate_email(email):
        return validate_email(email)