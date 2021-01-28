VOWELS = {'a', 'e', 'i', 'o', 'u'}


def vowel_filter(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [ch for ch in result if ch.lower() in VOWELS]

    return wrapper