import os

filename = input("Enter a filename: ")

if os.path.exists(filename):
    print("File exists!")
else:
    print("File not found!")