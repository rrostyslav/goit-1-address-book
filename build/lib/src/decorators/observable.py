from functools import wraps  # Імпортує wraps з functools для збереження метаданих функцій при використанні декораторів
import inspect  # Імпортує модуль inspect (хоча він не використовується в цьому коді)

# Декоратор класу, що додає можливість спостерігати за змінами
def observable(cls):
    cls._observers = {}  # Створює атрибут для зберігання спостерігачів

    # Метод для додавання спостерігача
    def add_observer(self, observer, observer_type):
        if observer_type not in self._observers:
            self._observers[observer_type] = []  # Створює новий список для спостерігачів, якщо тип не існує
        self._observers[observer_type].append(observer)  # Додає спостерігача до відповідного типу

    cls.add_observer = add_observer  # Додає метод add_observer до класу
    return cls

# Декоратор для методів, що повинні сповіщати спостерігачів про зміни
def notify_observers(observer_type):
    def decorator(method):
        @wraps(method)  # Зберігає оригінальні метадані методу, такі як __name__ та __doc__
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)  # Викликає оригінальний метод

            if result is not None:
                # Поєднує позиційні аргументи в kwargs['args'] і додає результат
                combined_kwargs = kwargs.copy()
                combined_kwargs['args'] = args
                combined_kwargs['result'] = result

                # Сповіщає всіх спостерігачів вказаного типу
                for observer in self._observers.get(observer_type, []):
                    observer(**combined_kwargs)

                return result  # Повертає результат виконання оригінального методу

        return wrapper

    return decorator
