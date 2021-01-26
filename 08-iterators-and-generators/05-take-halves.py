def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [x for _, x in zip(range(n), seq)]

    return take, halves, integers
