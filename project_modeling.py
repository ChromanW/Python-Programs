# Develop a chatting software

# Actors
# 1. User
# 2. Admin

# Featuers
# User
# 1. Login (Auth)
# 2. Signup
# 3. Connect (w/ other users)
# 4. Sending messages
# 5. Create a post
# 6. Delete account
# 7. View all posts
# 8. settings tab that gives access to changing ur password deleteing account and etc.
# 9. report option on accounts and postts

# Admin
# 1. Edit User Details
# 2. Delete a User
# 3. View all users
# 4. View all posts 
# 5. Edit a post
# 6. Delete a post
# 7. recive reports
# 8. time out users accounts for * amount of days
# 9. access to all user passwords

# Storage (Create files)
# 1. Sign up (Create a file to add all users) -> signup.txt
# 2. view posts -> posts.txt
# 3. connect to users -> connect.txt


# email = input('Enter your email address')
# password = input('Enter your password: ')

# if email == dict['email'] and password == dict['password']:
#     login()


# message = "Hi there  sdfdsf sdf dsf  sdf sf sf s -david"
# print(message.split('-'))


# Homework task
# Models for 
# use dict
# 1. User
# 2. Admin
# 3. Post
# 4. unique_email(email): check signup.txt and read the email





1.
user = {
    "username": "oliver_trand",
    "email": "trand.oliver@gmail.com",
    "password": "ijds8dk",
    "age": 30,
}

2.
admin = {
    "username": "Lander",
    "email": "lander@gmail.com",
    "password": "lander123",
    "age": 35,
    "role": "administrator",
    "perms": ["ban", "timeout", "update", "delete", "etc"]
}

3.
post = {
    "author": "Oliver trand",
    "email": "trand.oliver@gmail.com",
    "title": "At the park",
    "post time": "2024-02-05",
    "tags": ["park"],
    "likes": 50,
    "comments": "wow so cool," "etc"
}



