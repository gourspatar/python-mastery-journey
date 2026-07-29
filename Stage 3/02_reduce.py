from functools import reduce

numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)

# Find the sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

# Find the product
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)