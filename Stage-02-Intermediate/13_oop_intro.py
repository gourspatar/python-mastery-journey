# Program 1
# Create a Class & Create 2 Objects
class Car:
    pass

car1 = Car()
car2 = Car()

print(car1)
print(car2)

# Program 2
# Add Attributes To Class & Create 2 Objects
car1.brand = "Tesla"
car1.model = "S"
car2.brand = "BMW"
car2.model = "M5"
print(car1.brand, car1.model)
print(car2.brand, car2.model)

# Bonus Program
class FootballPlayer:
    pass

player1 = FootballPlayer()
player1.name = "Messi"
player1.position = "Right Winger"
print(player1.name, player1.position)
player2 = FootballPlayer()
player2.name = "Ronaldo"
player2.position = "Forward"
print(player2.name, player2.position)
player3 = FootballPlayer()
player3.name = "Neymar"
player3.position = "Forward"
print(player3.name, player3.position)