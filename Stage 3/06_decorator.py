def my_decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")
    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()