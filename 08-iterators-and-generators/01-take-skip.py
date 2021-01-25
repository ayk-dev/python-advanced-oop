class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0
        self.counter = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        value = self.current
        self.current += self.step
        if self.counter < self.count:
            self.counter += 1
            return value
        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)