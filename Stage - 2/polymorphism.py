# Program 1
# Animal Sound
class Animal:
    def sound(self):
        print("Some sound")


class Lion(Animal):
    def sound(self):
        print("Roar")

class Tiger(Animal):
    def sound(self):
        print("Growl")


class Elephant(Animal):
    def sound(self):
        print("Trumpeting")


animals = [Lion(), Tiger() , Elephant()]

for animal in animals:
    animal.sound()

# Program 2
# Employeee
class Employee:
    def sound(self):
        print("Some Work")


class Manager(Employee):
    def work(self):
        print("Managing the team...")

class Developer(Employee):
    def work(self):
        print("Writing Python code...")


class Designer(Employee):
    def work(self):
        print("Designing UI...")


employees = [Manager(), Developer() , Designer()]

for employee in employees:
    employee.work()
