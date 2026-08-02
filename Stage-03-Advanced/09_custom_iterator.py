class Counter:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 5:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration


counter = Counter()

for num in counter:
    print(num)