# Create The Text File
with open("example.txt", "w") as file:
    file.write("Hello, I'am Gour!\n")
    file.write("& Welcome to file handling.")

# Read the text file 
with open("example.txt", "r") as file:
    content = file.read()
    print(content)