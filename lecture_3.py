# Boolean operators
# these are used to combine more than one condition

# AND
# OR
# NOT

# Write a python program that takes a number as an input
# and checks if the number is divisible by 2 or 3 or by both
# 2^n 2^2 == 4

# only divisible by 2
# only divisible by 3
# divisible by both 2 and 3
# divisible by none

num = int(input("Enter a number: "))

# elif
if (num % 2 == 0) and (num % 3 == 0):
    print(num, "is divisible by both 2 and 3")
elif (num % 2 == 0):
    print(num, "is divisible only by 2")
elif (num % 3 == 0):
    print(num, "is divisible only by 3")
else:
    print(num, "is divisible by neither 2 nor 3")

# Write a pyton program that takes score(marks) as input
# and outputs the results as grades 
# (90 - 100) -> A
# (80 - 90) -> B
# (70 - 80) -> C
# (60 - 70) -> D
# (< 60) -> F

num = int(input("Enter a number: "))
if (num >= 90) and (num <=100):
  print(num, "is A")

elif (num >= 80) and (num <90):
   print(num, "is B")
elif (num >= 70) and (num <80):
    print(num, "is C")   
elif (num >= 60) and (num <70):
    print(num, "is D")

else:
    print("F")    