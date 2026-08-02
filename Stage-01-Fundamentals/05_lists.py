# Program -- 1
# Create a list of 5 favorite things.
favorite_things = ["Pizza", "Movies", "Traveling", "Music", "Reading"]
print(favorite_things[0])
print(favorite_things[4])
print(len(favorite_things))

favorite_things.append("Sports")
print(favorite_things)

favorite_things.remove("Movies")
print(favorite_things)

for things in favorite_things:
    print(things)

# Bonus
search = input("Enter a name: ")
if search in favorite_things:
    print(f"{search} is in the list.")
else:
    print(f"{search} is not in the list.")
