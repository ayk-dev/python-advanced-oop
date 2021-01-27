def logged(fn):
    def wrapper(*args):
        args_formatted = ', '.join(map(str, args))
        result = fn(*args)

        return '\n'.join([
            f"you called {fn.__name__}({args_formatted})",
            f"it returned {result}"
        ])

    return wrapper