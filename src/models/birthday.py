from datetime import datetime  # Імпортує клас datetime для роботи з датами
from src.models.field import Field  # Імпортує базовий клас Field, від якого наслідується клас Birthday

# Клас Birthday, що представляє дату народження контакту
class Birthday(Field):
    # Ініціалізатор класу Birthday
    def __init__(self, value):
        try:
            # Перетворює вхідний рядок у форматі DD.MM.YYYY на об'єкт datetime
            super().__init__(datetime.strptime(value, '%d.%m.%Y'))
        except ValueError:
            # Піднімає помилку, якщо формат дати неправильний
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
