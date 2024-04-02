import random 
import time
# Libraries in python
# Time
# Random

# Select a random number from a list
list = [1, 2, 5, 1, 33, 11, 45, 12, 78]
print(random.choice(list))

# Generate a random number
print(random.randint(0, 100))

# Shuffle the list
random.shuffle(list)
print(list)

# Generates a random number (0 - 1)
# for the first time
random.seed(5)
print(random.random())

# -----------------------------------

# Time all in seconds
seconds = time.time()
print(seconds)

# Print the local time
local_time = time.ctime(seconds)
print("Local Time: ", local_time) 

# Sleep
print("Print before sleep")
time.sleep(2.5)
print("Print After sleep")

# -----------------------------------
# Recursion in python
# Using a function inside itself
# Factorial of a given number
# num = 5
# fact -> 5 * 4 * 3 * 2 * 1 = 120

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)
    

# 5 * (24) = 120
# 4 * (6) = 24
# 3 * (2) = 6
# 2 * (1) = 2
# 1 * 1 = 1