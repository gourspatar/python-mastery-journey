class Mycontent:
    def __enter__(self):
        print("Entering...")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting...")


with Mycontent():
    print("Inside the block")