# Explict data types assignment in python
num:int = 45
print(num)

num:int = 34.67
print(num)

# Explict data types do not have an affect on Python

# Main Topic
# Functions
# 1. should only perfrom one functionality
# 2. to reduce the number of lines of code

# Types of functions
# 1. void type
# 2. return type

# A function might also take arguments/parameters
# Argument -> input value

# ---------- Void Type -----------
# Function Body
def greetings(name):
    print("Hi there how are you? ", name)

# Callback
greetings("David")

def info(name, age):
    print(name, "is", age, "years old")

info("David", 23)

# Default argument
def speak(name = "None"):
    print(name, "is speaking")

speak()

# -------------------- Return Type -------------------
def sum(num1:int, num2:int) -> int:
    return num1 + num2

print(sum(2, 4), sum(5, 4), sum(7, 7))

def max(list):
    max = list[0]
    for num in list:
        if num > max: 
            max = num

    return max

nums = [5, 1, 4, 8, 1, 2]
nums2 = [1, 3, 14, 48, 31, 122]
print(max(nums))
print(max(list = [1, 3, 14, 48, 31, 122]))

# Use of pass
def test():
    pass

test()

# Arbitrary Arguments, *args
# when you dont know total number of arguments
def display_people(*args):
    print(args[1], args[2], args[0])

display_people("john", "carl", "david", "fred", "sam")

# Homework
# 1. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
# Click me to see the sample solution

# 2. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]