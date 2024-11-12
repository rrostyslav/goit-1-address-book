from src.models.field import Field  # Імпортує клас Field, від якого наслідується Notes
from datetime import datetime  # Імпортує функції для введення та валідації даних
class Notes(Field):
    # Ініціалізатор класу Notes з можливістю додавання тегів
    def __init__(self, notes, tags=None):
        # Перевіряє, чи є нотатки рядком, і якщо ні, піднімає помилку
        if not isinstance(notes, str):
            raise ValueError("Notes must be a string")
        # Викликає ініціалізатор батьківського класу з переданими нотатками
        super().__init__(notes)
        # Зберігає дату та час створення нотатки
        self.created_at = datetime.now()
        # Ініціалізує теги, якщо вони не передані
        self.tags = tags if tags else []

    # Метод для представлення об'єкта Notes у вигляді рядка
    def __str__(self):
        # Повертає текст нотатки, дату її створення та список тегів у зрозумілому форматі
        tags_str = ", ".join(self.tags)
        return f"{self.value} (Created on: {self.created_at.strftime('%d.%m.%Y %H:%M')}) Tags: [{tags_str}]"

    def add_tag(self, tag):
            self.tags.append(tag)
            
    def has_tag(self, tag):
        # Перевіряє, чи містить нотатка заданий тег
        return tag in self.tags