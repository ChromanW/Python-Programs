import os

# File Handling in Python
# Why creating Files?
# Storing some information

# CRUD
# Create a new file
# 'x' -> create a new file
# 'a' -> append some data
# 'w' -> write some data (overwriting existing data)

file = open('file.txt', 'a')
data = "\nWe are learning python"
file.write(data)

# Delete old files
# try:
#     os.remove("file.txt")
# except FileNotFoundError:
#     print("File not found")

# Delete a folder
# os.rmdir("files")

# Read a file
# 'r' -> read the file
file = open("file.txt", "r")
data = file.readline()
# print(data)

# Reading the parts of a file
# read(the number of characters)
# for i in range(4):
#     data = file.readline()
# print(data)

# Read line by line
for line in file:
    print(line)
file.close()

# Close the file
# close()