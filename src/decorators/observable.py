from functools import wraps
import inspect

def observable(cls):
    cls._observers = {}

    def add_observer(self, observer, observer_type):
        if observer_type not in self._observers:
            self._observers[observer_type] = []
        self._observers[observer_type].append(observer)

    cls.add_observer = add_observer
    return cls


def notify_observers(observer_type):
    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)

            if result is not None:

                # Combine positional args into kwargs['args'] and add result
                combined_kwargs = kwargs.copy()
                combined_kwargs['args'] = args
                combined_kwargs['result'] = result

                # Notify all observers of the specified type
                for observer in self._observers.get(observer_type, []):
                    observer(**combined_kwargs)

                return result

        return wrapper

    return decorator