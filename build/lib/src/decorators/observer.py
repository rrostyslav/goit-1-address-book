from functools import wraps  # Імпортує wraps з functools для збереження метаданих функцій при використанні декораторів

# Декоратор класу для автоматичної реєстрації всіх спостерігачів
def observer_class(cls):
    original_init = cls.__init__  # Зберігає оригінальний метод __init__ класу

    # Новий метод ініціалізації, що додає спостерігачів
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)  # Викликає оригінальний ініціалізатор класу

        # Реєструє спостерігачів, які мають атрибут 'is_observer' встановлений у True
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and getattr(attr, 'is_observer', False):
                observer_type = getattr(attr, 'observer_type', None)
                self.__model__.add_observer(attr, observer_type)  # Додає спостерігач до моделі

    cls.__init__ = new_init  # Заміщує оригінальний метод __init__ новим методом
    return cls

# Декоратор для методів, що стають спостерігачами
def observer(observer_type):
    def decorator(method):
        @wraps(method)  # Зберігає оригінальні метадані методу, такі як __name__ та __doc__
        def wrapper(*args, **kwargs):
            return method(*args, **kwargs)  # Викликає оригінальний метод
        # Додає атрибути до методу, щоб ідентифікувати його як спостерігача
        wrapper.is_observer = True
        wrapper.observer_type = observer_type
        return wrapper
    return decorator
