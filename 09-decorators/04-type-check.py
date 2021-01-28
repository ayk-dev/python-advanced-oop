def type_check(_type):
    def wrapper(func):
        def wrapped(arg):
            if not isinstance(arg, _type):
                return "Bad Type"
            return func(arg)
        return wrapped
    return wrapper


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))