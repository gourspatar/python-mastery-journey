class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


book = Book("Atomic Habits", "James Clear")

print(book)
print(str(book))     # healpful for users .. nice outputs
print(repr(book))    # helpful for us .. best for debugging and detailed