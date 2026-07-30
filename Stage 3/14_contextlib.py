from contextlib import contextmanager


@contextmanager
def my_context():
    print("Entering the context")

    yield

    print("Exiting the context")


with my_context():
    print("Inside the context")