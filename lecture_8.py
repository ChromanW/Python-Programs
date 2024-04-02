# Time complexity 
# Space complexity
# Best case O(1) and a worst case O(n)

# numbers = [1, 6, 2, 4, 6, 8]
# searched_value = int(input("Enter the number to search: "))

# for num in numbers:
#     if num == searched_value:
#         print('Found value!')
#         break

# Nested Loops
# loop inside another loop
# O(n^2)

# matrix
# row
# column
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[1][2])

# using for-each
for row in matrix:
    for column in row:
        print(column, end=' ')
    print()

# for loop
# print(len(matrix)) # prints total number of rows
# print(len(matrix[0])) # prints the length of the first row
print()

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=' ')
        # print(matrix[row][col], '[', row, col, ']', end=' ')
    print()

rows = int(input('Please provide number of rows: '))
columns = int(input('Please provide number of columns: '))

# rows = 5
# columns = 5
for row in range(rows):
    for col in range(columns):
        print('#', end=' ')
    print()

#
# #
# # #
# # # #
# # # # #

print()

# i -> row
# j -> column
for i in range(rows + 1):
    for j in range(i + 1):
        print('#', end=' ')
    print()

# Homework task
        #
      # #
    # # #
  # # # # 
# # # # # 
    
# reterive the data using a while loop
    
for i in range(rows + 1):
    for j in range(i + 1):
        print('#', end=' ')
    print()