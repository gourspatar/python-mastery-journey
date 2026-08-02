def outer():
    message = "Hello from outer!"

    def inner():
        print(message)

    return inner


my_function = outer()
my_function()