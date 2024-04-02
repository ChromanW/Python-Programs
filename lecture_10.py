# Dictionaries
# Hash Map / JSON / Object
# key : value

# Person's attributes
email = "abc@example.com"
password = "*******"
name = "David"
age = 24

# Whenever you need to represent a physical entity
# we use dictionaries

# First: Find the entities of your app
# Second: Find the attributes of the entities

# Person's object
person = {
    "email": "",
    "password": "",
    "name": "",
    "age": 10
}

# Access the attributes of dict
# print(person["age"])

# Assign/update value to the attributes
person['name'] = 'John Smith'
person['fav_color'] = 'White' # not 
# print(person['fav_color'])

# pop/delete value from dict
person.pop('age')

# loop through the dict
for key, value in person.items():
    print(key, ':', value)


# nested dictionaries
# Create an app for a school
# 1. students
# 2. courses

course = {
    'course_id': '',
    'course_name': '',
    'credit_hours': '',
}
student = {
    'name': 'Sam',
    'age': 24,
    'reg_no': 'Fall-20-12',
    'courses': [
        {
            'course_id': 'CSE105',
            'course_name': 'Computer Science',
            'credit_hours': '3,0',
        },
        {
            'course_id': 'CSE116',
            'course_name': 'Introduction to Python',
            'credit_hours': '4,0',
        }
    ],
}

# --------------- USE CASE --------------------
# Database
users = []

# Ask the user input for signup
# person['email'] = input("Please provide your email address: ")
# person['password'] = input("Please provide your password: ")
# person['name'] = input("Please provide your name: ")
# age = int(input("Please provide your age: "))
# if (age >= 18):
#     person['age'] = age 
# else:
#     print("Please enter the valid age")

# Add the data to the database
# users.append(person)

# print(users)


# Access a value from dictionary

# Homework Questions
# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Print the value of key ‘history’ from the below di 
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# Write a program to rename a key city to a location in the following dictionary.
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }




#1- Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
merged_dict = dict1

print(merged_dict)



#2- Print the value of key ‘history’ from the below di 
sampleDict = {
     "class": {
         "student": {
             "name": "Mike",
             "marks": {
                 "physics": 70,
                 "history": 80
             }
         }
     }
 }

print(sampleDict['class']['student']['marks']['history'])


#3- Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
   "name": "Kelly",
   "age":25,
   "salary": 8000,
   "city": "New york"
 }

sample_dict.pop('city')
sample_dict['location'] = "New york"
print(sample_dict)