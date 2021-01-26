class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current = count

    def __iter__(self):
        return self

    def __next__(self):
        val = self.current
        if self.current >= 0:
            self.current -= 1
            return val
        raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")