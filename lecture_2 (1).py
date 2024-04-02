# input function
# Take an input from the user

# Type casting
# Convert one datatype to another
# str -> int
num = int(input("Enter a number: "))
print(num + 20)

# ASCII
# abc
# abc12234@! 
print(chr(70))


# green color -> 70-100
# yellow -> 30 - 70
# red < 30

# Control Structure
# if (condition) 
# else

# Write a python program that takes a number as an input
# and determines if the number is even or odd

# 4, 6 -> Even
# 5, 7 -> Odd

# 2 / 2 -> 1
# % -> mod -> remainder

# Operators
# > greater than
# >= greater than and equal to
# < smaller than
# <= smaller than or equal to
# = assignment operator
# == is equal to
# != is not equal to

if num % 2 == 0:
    print(num, "Even")
else:
    print(num, "Odd")

# Pygame
# Tkinter

# Write a python program that takes a number as an input
# and determines if the number is positive or negative

num = int(input ("enter a number: "))

if num > 0:
      print(num, "positive")
else:
     print(num, "negitave")      