# Program 1
class Animal:
    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.bark()

# Program 2

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    pass

car = Car("Tesla")
print(car.brand)