# for loop
# Write a python program that displays the first 10 integers

# range(start, end, step)
# for i in range(10):
#     print(i)

# Print the list in reverse order
numbers = [4, 3, 1, 55, 12, 66, 78, 90, 15]

# left to right
# start = 0
# end = len(numbers)
# step = 1

# right to left
# start = len(numbers) - 1 
# end = 0
# step = 1 # start = start - step

count = len(numbers) - 1
while count >= 0:
    print(numbers[count])
    count-=1

print()
for i in range(len(numbers) - 1, 0, -1):
    print(numbers[i])

# create two lists one is grades and the other one is string (names)
# step by step process
# [45, 12, 56, 90]
# ['Sam', 'David', 'Carol', 'Sarah']
# final list
# ['Sam', 45, David, 12]
# print all the items both in forward and reverse order

grades = [45, 12, 56, 90] # 6
names = ['Sam', 'David', 'Carol', 'Sarah'] # 4

final = []

# == -> is equal to
# != -> is not equal to
if (len(grades) != len(names)):
    print("Cannot add into a new list because of different length")
else:
    for i in range(len(grades)):
        final.append(names[i])
        final.append(grades[i])

    print(final)    

# for-each loop
# for each item inside a list
# strings
# lists
# tuple
# set
# dictionary(keys, values)
for name in names:
    print(name)

for grade in grades:
    print(grade)


# for i in range(10):
#     print(i)

# str = 'Python'
# for char in str:
#     print(char)

# Statements 
# break -> breaks the loop
# continue -> skip certain values

print()

for i in range(10):

    if i == 5:
        break
    print(i)

i = 0
while True:
    print("Hello")
    i+=1
    if i == 45:
        break

print()
for i in range(100):
    # if i % 5 == 0:
    if i >= 25 and i <= 50:
        continue
    print(i)


print()
# ----------------------------------------------------------------
# max value in list
list = [1, 2, 5, 11, 9, 6, 4]
# 1, 15, 6, 8
# 15, 6, 8
# 15, 8
# 15

max = 0 #1
for num in list:
    # 1, 2, 5, 11, 
    if num >= max:
        max = num

print(max)
