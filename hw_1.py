# max value in list
list = [1, 2, 5, 11, 9, 6, 4]
# 1, 15, 6, 8
# 15, 6, 8
# 15, 8
# 15

min = 0 #1
for num in list:
    # 1, 2, 5, 11, 
    if num >= min:
        min = num

print(min)

# steps
# 1. travel through the list
# 2. compare each value with the max set
# if the comming value is larger than the max
# max = comming value
# at the end -> display max value

str = "aaatatfaf"
i = 0
for char in str:
    if char == "a":
        i += 1

print(i)

print()

#1.travel through the string, use a loop to travel through the string.
#2. count the char of your choice inside the string
#3. Create a variable and store the occurences of a single char
#4. print out the variable




#Questions

#Print all even numbers from 1 to 20
#2.. Reverse a string:
#3. Calculate the sum of squares of numbers from 1 to 10:
#4. Find the largest element in a list:
#5. Count the occurrences of each character in a string:

start = 1
end = 21
for i in range (start, end):
    if i %2 == 0:
        print(i, "is even")
print()  

    # ----------------------------------------------------------------
# max value in list
list = [2, 5, 11, 9, 1, 6, 4]
# 1, 15, 6, 8
# 15, 6, 8
# 15, 8
# 15

min = list [0]
for num in list:
    # 1, 2, 5, 11, 
    if num <= min:
        min = num

print(min)

# steps
# 1. travel through the list
# 2. compare each value with the max set
# if the comming value is larger than the max
# max = comming value
# at the end -> display max value



#reverse a strin


string = "we love earth"
new_string = ""
for i in range(len(string)- 1, 0, - 1):
    new_string += string[i] 

print(new_string)

#_________________________________________________
#Find the sum of squares of numbers from 1 t o10
# need to from 1 to 10
# for each number calculate the square
# 2 -> print(2 ** 2)
#sum = 0

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for num in list:
    square = num **2
    sum += square

print(sum)