# program -- 1
# Print numbers from 1 to 10 using a while loop.

c = 1
while c <= 10:
    print(c)
    c += 1

# program -- 2
# Print even numbers from 2 to 20 using a while loop.
c = 2
while c <= 20:
    print(c)
    c += 2 

# program -- 3
# Ask the user to guess a secret number ...
#  Keep asking until they guess correctly !!

print("Guess the secret number between 1 and 10")
secret_number = 7
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Wrong guess. Try again.")

# program -- 4
# Create a menu:

while True:
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You selected Option 1.")
    elif choice == 2:
        print("You selected Option 2.")
    elif choice == 3:
        print("You selected Option 3.")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")