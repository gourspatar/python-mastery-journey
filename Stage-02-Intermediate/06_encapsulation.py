# # Program 1
class Person:
    def __init__(self, name):
        self.__name = name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name
    
person1 = Person("Gour")
print(person1.get_name())
person1.set_name("Messi")
print(person1.get_name())

# Program 2
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount()

account.deposit(1000)
account.withdraw(300)
print("Current Balance:", account.get_balance())

account.withdraw(800)
account.deposit(-50)

# Bonus Program
class Person:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        if len(name) < 3:
            print("Name must have at least 3 characters.")
        else:
            self.__name = name

    def get_name(self):
        return self.__name

person = Person()
person.set_name("Go")
person.set_name("Gour")
print(person.get_name())