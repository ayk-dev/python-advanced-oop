class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        idx = self.iterations % len(self.sequence)
        if self.iterations < self.number:
            self.iterations += 1
            ch = self.sequence[idx]
            return ch
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')