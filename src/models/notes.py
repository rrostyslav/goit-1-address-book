from datetime import datetime
from src.models.field import Field

class Notes(Field):
    def __init__(self, notes):
        if not isinstance(notes, str):
            raise ValueError("Notes must be a string")
        super().__init__(notes)
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.value} (Created on: {self.created_at.strftime('%d.%m.%Y %H:%M')})"