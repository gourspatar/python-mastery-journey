# Program 1
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = student("Gour", 19)
print(student1.name)
print(student1.age)
student2 = student("Rahul", 20)
print(student2.name)
print(student2.age)

# Program 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Atomic Habits", "James Clear")
print(book1.title)
print(book1.author)
book2 = Book("Deep Work", "Cal Newport")
print(book2.title)
print(book2.author)

# Bonus Program
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
account1 = BankAccount("Gour", 10000000000000000000000000000000)
print(f"Account Holder: {account1.name}")
print(f"Account Balance: {account1.balance}")