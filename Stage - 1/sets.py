# Program 1

# Create a set:
fruits = {"Apple", "Banana", "Orange", "Apple"}
# apple appears onlybonce in the set, as sets do not allow duplicates.
print(fruits)

# Program 2
# Add an item to the set:
fruits.add("Mango")
print(fruits)

# Program 3
# Remove: banana from the set:
fruits.remove("Banana")
print(fruits)

#Program 4
# Use a for loop to print all items.
for fruit in fruits:
    print(fruit)

# Program 5
# Check if "Orange" exists in the set.
if "Orange" in fruits:
    print("Orange is in the set.")

# Bonus Challenge
# Create two sets:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
#Print:
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)

