# Program - 1
# Print -- Hello, Python!
def say_hello():
    print("Hello, Python!")

# Call the function
say_hello()


# program - 2
# Hello, Gour! .. with parameters !!
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Gour")


# program - 3
# Return the sum of two numbers.
def add(a, b):
    return a + b

# Call the function
result = add(5, 3)
print(result)


# Return True if the number is even, otherwise False.
def is_even(number):
    return number % 2 == 0

# Call the function
print(is_even(4))  # True
print(is_even(7))  # False

#Print:
#Addition
#Subtraction
#Multiplication
#Division .. using python functions

def calculator(a, b):
    return a + b, a - b, a * b, a / b

# function call
print(calculator(10, 5))