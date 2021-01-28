def even_numbers(function):

    def wrapper(numbers):

        result = function(numbers)
        return [n for n in result if n % 2 == 0]

    return wrapper