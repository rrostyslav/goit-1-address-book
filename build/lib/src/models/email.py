import re  # Імпортує модуль для роботи з регулярними виразами (не використовується в цьому конкретному коді)
from src.models.field import Field  # Імпортує базовий клас Field, від якого наслідується клас Email
from src.utils.validations import validate_email  # Імпортує функцію для валідації електронної адреси

# Клас Email, що представляє електронну адресу контакту
class Email(Field):
    # Ініціалізатор класу Email
    def __init__(self, email):
        # Перевіряє правильність формату електронної адреси, і якщо вона неправильна, піднімає помилку
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        # Викликає ініціалізатор батьківського класу з переданою електронною адресою
        super().__init__(email)

    # Статичний метод для перевірки електронної адреси
    @staticmethod
    def validate_email(email):
        # Використовує імпортовану функцію validate_email для перевірки формату електронної адреси
        return validate_email(email)
