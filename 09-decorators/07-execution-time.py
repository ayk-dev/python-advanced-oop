import time


def exec_time(func):
    def wrapped(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        return after - before
    return wrapped


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 1_000_000))