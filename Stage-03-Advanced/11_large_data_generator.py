def large_data():
    for num in range(1, 1_000_001):
        yield num


generator = large_data()

# _ bcz i am intentionally ignoring the loop variable...
for _ in range(10):
    print(next(generator))