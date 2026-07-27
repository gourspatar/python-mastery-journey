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