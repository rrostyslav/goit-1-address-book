from src.models.field import Field

class Name(Field):
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        super().__init__(name)