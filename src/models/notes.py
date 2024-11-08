from datetime import datetime  # Імпортує клас datetime для роботи з датою та часом
from src.models.field import Field  # Імпортує базовий клас Field, від якого наслідується клас Notes

# Клас Notes, що представляє нотатки для контакту
class Notes(Field):
    # Ініціалізатор класу Notes
    def __init__(self, notes):
        # Перевіряє, чи є нотатки рядком, і якщо ні, піднімає помилку
        if not isinstance(notes, str):
            raise ValueError("Notes must be a string")
        # Викликає ініціалізатор батьківського класу з переданими нотатками
        super().__init__(notes)
        # Зберігає дату та час створення нотатки
        self.created_at = datetime.now()

    # Метод для представлення об'єкта Notes у вигляді рядка
    def __str__(self):
        # Повертає текст нотатки та дату її створення у зрозумілому форматі
        return f"{self.value} (Created on: {self.created_at.strftime('%d.%m.%Y %H:%M')})"
