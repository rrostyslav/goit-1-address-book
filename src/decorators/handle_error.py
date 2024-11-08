from functools import wraps  # Імпортує wraps з functools для збереження метаданих функцій при використанні декораторів

# Декоратор для обробки помилок у методах
def handle_error(method):
    @wraps(method)  # Зберігає оригінальні метадані методу, такі як __name__ та __doc__
    def wrapper(self, *args, **kwargs):
        try:
            # Викликає оригінальний метод
            return method(*args, **kwargs)
        except Exception as e:
            # Обробляє будь-яку виниклу помилку і виводить її
            print(e)
    return wrapper
