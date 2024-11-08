from src.models.field import Field

class Address(Field):
    def __init__(self, address):
        if not isinstance(address, str) or not address:
            raise ValueError("Address must be a non-empty string")
        super().__init__(address)