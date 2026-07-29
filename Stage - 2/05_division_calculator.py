# Program 1
# division_calculator
try:
    print("Please enter any two number :")
    x = int(input("enter a = "))
    y = int(input("enter b = "))

    print(x / y)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Please enter a valid number!")

else:
    print("Everything worked!")

finally:
    print("Program finished.")

# Program 2
# age_validator Program

print("Please enter Your Age :")
age = int(input(" Age = "))

if age <= 0 :
    raise ValueError("Invalid age!")

else:
    print("Age accepted!")

# Bonus Program 
# simple_bank_system 

balance = 1000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance!")

    balance -= amount
    print("Withdrawal successful!")
    print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)
