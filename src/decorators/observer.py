from functools import wraps

# Декоратор класу для автоматичної реєстрації всіх спостерігачів
def observer_class(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)

        # Реєстрація спостерігачів за типом
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and getattr(attr, 'is_observer', False):
                observer_type = getattr(attr, 'observer_type', None)
                self.__model__.add_observer(attr, observer_type)

    cls.__init__ = new_init
    return cls

def observer(observer_type):
    def decorator(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            return method(*args, **kwargs)
        # Add observer type as an attribute to the method
        wrapper.is_observer = True
        wrapper.observer_type = observer_type
        return wrapper
    return decorator
