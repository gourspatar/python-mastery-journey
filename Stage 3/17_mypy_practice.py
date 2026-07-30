def multiply(a: int, b: int) -> int:
    return a * b


print(multiply("2", "3"))

# will give error when you run using mypy 
# bcz you are passing string instead of int ..