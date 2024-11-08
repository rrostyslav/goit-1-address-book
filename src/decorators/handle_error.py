from functools import wraps

def handle_error(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper