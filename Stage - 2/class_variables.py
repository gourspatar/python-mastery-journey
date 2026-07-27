# program - 1
class Employee:
    company = "Anthropic"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)
print(employee1.name)
print(employee1.salary)
print(employee1.company)
print(employee2.name)
print(employee2.salary)
print(employee2.company)

# Program - 2

class Employee:
    #company = "Google"
    def __init__(self, name, salary , company):
        self.name = name
        self.salary = salary
        self.company = company

employee1 = Employee("Alice", 50000 , "Google")
employee2 = Employee("Bob", 60000 , "Google")
print(employee1.name)
print(employee1.salary)
print(employee1.company)
print(employee2.name)
print(employee2.salary)
print(employee2.company)

# Bonus Challenge

class FootballClub:
    league = "La Liga"
    def __init__(self,club_name,stadium):
        self.club_name = club_name
        self.stadium =  stadium
        FootballClub.league = "Champions League"

FootballClub1 = FootballClub("Barcelona","Barcelona Stadium")
FootballClub2 = FootballClub("Real Madrid","Madrid Stadium")

print(FootballClub1.club_name)
print(FootballClub1.stadium)
print(FootballClub1.league)
print(FootballClub2.club_name)
print(FootballClub2.stadium)
print(FootballClub2.league)
