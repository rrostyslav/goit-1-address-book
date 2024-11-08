from datetime import datetime
from src.models.field import Field

class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, '%d.%m.%Y'))
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")