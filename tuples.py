# Program 1
# Create a tuple of 5 programming languages.
programming_languages = ("Python", "Java", "C++", "JavaScript", "Ruby")
print(programming_languages[0])
print(programming_languages[4])
print(len(programming_languages))

# Program 2
# Use a for loop to print all languages.
for language in programming_languages:
    print(language)

# Program 3
# Check if "Python" exists in the tuple.
if "Python" in programming_languages:
    print("Python is in the tuple.")

# Bonus Challenge
programming_languages[0] = "Java"
# --Tuple is immutable ...