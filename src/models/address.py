from src.models.field import Field  # Імпортує базовий клас Field, від якого наслідується клас Address

# Клас Address, що представляє адресу контакту
class Address(Field):
    # Ініціалізатор класу Address
    def __init__(self, address):
        # Перевіряє, чи є адреса рядком і чи вона не є порожньою, якщо ні, піднімає помилку
        if not isinstance(address, str) or not address:
            raise ValueError("Address must be a non-empty string")
        # Викликає ініціалізатор батьківського класу з переданою адресою
        super().__init__(address)
