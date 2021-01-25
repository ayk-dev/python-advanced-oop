class CustomRangeIterator:
    def __init__(self, start, end):
        self.index = start
        self.end = end

    def __next__(self):
        if self.index <= self.end:
            index = self.index
            self.index += 1
            return index
        raise StopIteration()


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return CustomRangeIterator(self.start, self.end)


one_to_five = custom_range(1, 5)
for num in one_to_five:
    print(num)