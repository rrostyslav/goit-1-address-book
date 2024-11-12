import re  # Імпортує модуль для роботи з регулярними виразами (не використовується в цьому конкретному коді)
from src.models.field import Field  # Імпортує клас Field, від якого наслідується клас Phone
from src.utils.validations import validate_phone  # Імпортує функцію для валідації номера телефону

# Клас Phone, що наслідується від Field
class Phone(Field):
    # Ініціалізатор класу Phone
    def __init__(self, phone):
        # Перевіряє правильність формату номера телефону, і якщо він неправильний, піднімає помилку
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format. Use +380XXXXXXXXX")
        # Викликає ініціалізатор батьківського класу з номером телефону
        super().__init__(phone)

    # Статичний метод для перевірки номера телефону
    @staticmethod
    def validate_phone(phone):
        # Використовує імпортовану функцію validate_phone для перевірки номера телефону
        return validate_phone(phone)
