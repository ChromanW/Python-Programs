#QUIZ Questions:

#1. The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
#For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

#2. Use a loop to display elements from a given list present at odd index positions
#my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#3. Print the following pattern
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5

#4. WAP to separate positive and negative number from a list.
#Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
#Expected output 
#Result:
#Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]

#5. Write a Python program that asks the user to enter a series of numbers, terminated by a zero. Use a while loop to collect the input, and then a for loop to calculate and print the sum and average of the non-zero numbers.



#1-
List = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list)


#2- 
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(my_list), 2):
    print(my_list[i])


#3-

rows = int(input('Number of rows: '))
columns = int(input('Number of columns: '))

#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5

for i in range(rows + 1):
    for j in range(i + 1):
        print('1', end=' ')
    print()




#4-




#5- 
