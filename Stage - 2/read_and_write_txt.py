name = input("Enter your name :")

with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    stored_name = file.read()

print("Name from file:", stored_name)