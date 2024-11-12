from src.models.field import Field  # Імпортує базовий клас Field, від якого наслідується клас Name

# Клас Name, що представляє ім'я контакту
class Name(Field):
    # Ініціалізатор класу Name
    def __init__(self, name):
        # Перевіряє, чи є ім'я рядком і чи воно не є порожнім, якщо ні, піднімає помилку
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        # Викликає ініціалізатор батьківського класу з переданим іменем
        super().__init__(name)
