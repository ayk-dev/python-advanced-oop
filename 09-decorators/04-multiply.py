def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs) * times

        return wrapper

    return decorator