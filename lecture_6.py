# Repetition Structure
# Loops

# While
# for each 
# for

# Write a python program that displays first 10 integers on the screen

start = 1
end = 10
step = 1

# Until loop
while (start <= end) :
    print(start) # 1, 2
    start = start + step # start = 1 + 1, start = 2 + 1

print()


count = 1
while (count <= 10):
    print(count) 
    count+=1 # count = count + 1

print()
# actual = 5
# while (int(input("Enter the guess number: ")) != actual):
#     print("You have guessed the wrong number\nPlease try again!")

# print("You guessed it right")


# Write a python program that prints firsts 100
# numbers that are divisible by both 2 and 3

start = 1
end = 100
step = 1

# condition for the loop
while(start <= end):
    # condition for the problem
    if (start % 2 == 0) and (start % 3 == 0):
        print(start, "is divisible by both 2 and 3")
    
    start = start + step


# sum the first 10 numbers
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = sum

start = 1
end = 100
step = 1
sum = 0
while(start <= end):
    if (start % 7 == 0):
     sum = sum + start
     print(sum)

    
    start = start + step   




# Create a multiplication table
# Ask the user about the input number

# Example
# input = 2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20
num = int(input ("enter a number: "))
start = 1
end = 10
step = 1
sum = 0
while(start <= end):
    sum = sum + num
    print(sum)
    start = start + step   




    #create a list of numbers and calculate the total number of even and odd numbers


list = [1, 2, 4]

start = 0
step = 1
end = 3
while( start != end):
    print(list[start])
    start = start + step



numbers = [28, 29, 76, 92, 53, 81, 94, 17, 12, 79]

even_count = 0
odd_count = 0

start = 0
end = 10
step = 1
while( start != end):
    number = numbers[start]
    if number %2 == 0:
        even_count += 1
    else:
        odd_count += 1
    start = start + step

print (even_count, odd_count)