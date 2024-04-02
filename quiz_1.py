# Questions:
#se an if statement to check whether a variable temperature is greater than 30. If it is, print "It's hot!".            done
#Create two string variables, first_name and last_name, and concatenate them to form a full name. Print the result.    done
#Define a string variable sentence with the value "Python is awesome!" What is the third character in the string?     done
#Create a list fruits with the elements "apple", "orange", and "banana". Add the element "grape" to the list.        done
#Given the list numbers = [1, 2, 3, 4, 5], what is the value at index 2?                                            done
#Declare a tuple colors with the elements "red", "green", and "blue". Can you change the value of the second element to "yellow"?       done
#Create two sets, set1 and set2, each containing three elements. Find the intersection of these sets.                                  done
 

weather = int(input("Enter a Tempature: "))
if  (weather >30):
  print(weather, "Its's hot!")


firstName = "Oliver"
lastName = "Arar"
fullName = firstName + " " + lastName
print(fullName)

cart = ['apple', 'orange', 'banana']
print(cart)

cart.insert(1, 'grape')
print(cart)


elements = ("red", "green","blue")
print(elements)

elements.remove("Green")
print(elements)

elements.add("yellow")
print(elements)


Message = "python is awesome!"
print(Message)



num1 = {1, 2, 3}
num2 = {2, 3, 4}

print(num1.intersection(num2))



# Define a string variable sentence with the value "Python is awesome!"
# What is the third character in the string?

sentence = 'Python is awesome'
print(sentence[2])

# Given the list numbers = [1, 2, 3, 4, 5]
# what is the value at index 2?

numbers = [1, 2, 3, 4, 5]
print(numbers[2])

# Create two sets, set1 and set2, each containing three elements.
# Find the intersection of these sets.

set1 = {1, 5, 2}
set2 = {6, 7, 2}
print(set1.intersection(set2))