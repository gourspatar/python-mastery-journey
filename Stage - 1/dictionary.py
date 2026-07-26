# program 1
# Print all four values.
person = {
    "name": "Gour",
    "age": 19,
    "favorite_player": "Messi",
    "country": "India"
}
print(person["name"])
print(person["age"])
print(person["favorite_player"])
print(person["country"])

# Program 2
# Add a new key-value pair to the dictionary and print the updated dictionary.
person["language"] = "Python"
print(person)

# program 3
# Update the age value and print the updated dictionary.
person["age"] = 20
print(person)

# problem 4
# Remove the "country" key-value pair from the dictionary and print the updated dictionary.
person.pop("country")
print(person)

# program 5 
for key, value in person.items():
    print(key, value)

# Bonus Challenge
# Ask the user:
#key = input("Enter a key: ")
#If the key exists:
#print(person[key])

key = input("Enter a key: ")
if key in person:
    print(person[key])
else:
    print(f"{key} does not exist in the dictionary.")
