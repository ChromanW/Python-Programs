# Lists
# Allows you to store more than one item

# item_1 = 'Cookies'
# item_2 = 'Fruits'
# item_3 = 'Vegetables'

cart = ['Cookies', 'Fruits', 'Vegetables', 'Meat']
print(cart)

# Add a new item to the list
# 1. Append()
cart.append('Eggs')
print(cart)

# 2. Insert(index, item)
cart.insert(1, 'Ketchup')
print(cart)

# Remove from the list
# 1. Remove('value')
cart.remove('Ketchup')
print(cart)

# 2. Pop(index) -> default index (len(list) - 1)
cart.pop(2)
print(cart)

# Sort (Ascending or descending)
nums = [1, 5, 12, 45, 23, 67, 45, 45, 45]
nums.sort(reverse=True)
print(nums)

chars = ['z', 'a', 'c', 'g', 'b', 'd', 'e', 'f']
chars.sort()
print(chars)


# Dynamic list
var = 45
var = "String"

# ["Name", "Age", "Gender", "Grades"]
dynamic_list = ["Sam", 24, "Male", 3.68]

# In python you cannot create a actual constansts
# only have representation
COMPANY = "Tesla"

# Tuples
rgb = (255, 255, 255)

# Sets
# It only carries unique values
number_set = {1, 5, 12, 45, 23, 67, 45, 45, 45}
print(number_set)

# unique functions
# union
# intersection
# difference

num1 = {1, 2, 3, 4}
num2 = {4, 2, 3, 6, 7, 8}

# Union -> combination of more than 2 sets 
print(num1.union(num2))

# intersection -> common elements of more than 2 sets
print(num1.intersection(num2))

# difference
print(num2.difference(num1))
