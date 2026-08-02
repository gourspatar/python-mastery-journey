# 03_generators.py

def even_numbers():
    for num in range(2, 11, 2):
        yield num


for number in even_numbers():
    print(number)