# QUIZ
# MAKE SURE TO PROVIDE A SIMPLE SOLUTION
# Write a Python program that takes a list of numbers as input and prints only the even numbers in the list.

# Define a function called calculate_discount that takes two arguments: price and discount_percentage. The function should calculate and return the discounted price based on the given percentage.

# Write a Python program that asks the user to input two numbers and performs division. Handle the ZeroDivisionError exception if the second number is zero.

# Create a text file named "sample.txt" and write some text into it using Python code. Then read and print the content of the file.

# Write a Python program that takes a string as input and prints the string in reverse order.

# Write a Python program to find the largest number in a given list and print its index.

# Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string and prints the count.

#modify the current solution by taking 5 numbers as an input and then finding the even numbers.
#convert the current solution as a function. return the even numbers as a list




1.
# numbers = input("Enter 5 numbers: ").split()
# even_nums = [num for num in numbers if num % 2 == 0]

def find_even_num (numbers):  
    even_nums = [ num for num in numbers if num % 2 == 0]
    return even_nums

def main():
    numbers = []
    for i in range(5):
        num = int(input("Enter numbers {}: ".format(i+1)))
        numbers.append(num)
    even_nums = find_even_num(numbers)

    print("even numbers:", even_nums)

if __name__ == "__main__":
    main()






2.
def calculate_discount(price, discount_percent, tax_price):
    discount_amount = price * (discount_percent / 100)
    tax_price = price * (tax_price / 100)
    discounted_price = price - discount_amount + tax_price
    return discounted_price

original_price = 100
discount_percent = 20
tax_price = 5
discounted_price = calculate_discount(original_price, discount_percent, tax_price)
print("Discounted price:" "Tax price:", discounted_price, tax_price)




3.
try:
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    num1 = int(num1)  #<----- this converts into integers
    num2 = int(num2)

    result = num1 / num2
    print("division results:", result)
except ValueError:
    print("Error: Enter valid number.")
except ZeroDivisionError:
    print("Error: You cant divide by zero")



4.
with open("sample.txt", "w") as file:
    file.write("Hello")

with open("sample.txt", "r") as file:
    print("Content of 'sample.txt':")
    print(file.read())


5.
input_string = input("Enter desired sentence: ")

print("Reverse string:", input_string[::-1])


6.
numbers = [4, 9, 2, 7, 5, 11, 8]

max_number = numbers [0]
max_index = 0

for i in range(1, len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
        max_index = i

print("The largest number iss:", max_number)
print("Its index in the list is:", max_index)



7.
input_string = input("Enter Characters: ")

vowel_count = sum(1 for char in input_string if char.lower() in 'aeiou')

print("Number of vowels:", vowel_count)









input_string = input("Enter a string:")
reverse_string = ""

for i in range (len(input_string) - 1, 0, -1):
    reverse_string += input_string[i]

print(reverse_string)