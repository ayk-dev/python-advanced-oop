def even_parameters(fn):
    def wrapper(*args):
        result = [n for n in args if isinstance(n, int) and n % 2 == 0]
        if len(result) == len(args):
            return fn(*args)
        else:
            return 'Please use only even numbers!'
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))