# Create a list from 1 to 10
# Use map() to square each number
# Use filter() to get even numbers

numbers = list(range(1, 11))
print("Original:", numbers)

squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)