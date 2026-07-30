import json

user = {
    "name": "Gour",
    "city": "Kolkata"
}

with open("user.json", "w") as file:
    json.dump(user, file)

# Read from user.json
with open("user.json", "r") as file:
    data = json.load(file)

print(data)