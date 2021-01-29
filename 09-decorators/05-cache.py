def cache(func):
    log = {}

    def wrapper(arg):
        if arg not in log:
            result = func(arg)
            log[arg] = result
            return result
        return log[arg]
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci.log)