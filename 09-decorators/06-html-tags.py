def tags(tag):
    def wrapper(func):

        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{tag}>{result}</{tag}>'

        return wrapped
    return wrapper


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))