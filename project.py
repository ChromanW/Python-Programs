def unique_email(email) -> bool :

    file = open("signup.txt", "r")    
    for line in file:
        if email in line:
            return False
    return True

# print(unique_email("john.smith@gmail.com"))

# password must contain at least 8 characters
# password must contain at least one small letter and capital letter
# password must contain at least one alphanumeric character
def check_alphabet(password) -> bool :

    # char = 'Pass12'
    is_small = False
    is_capital = False
        
    for char in password:
        # capital case alphabets
        if (ord(char) >= 65 and ord(char) <= 90):
            is_capital = True
        # Small case alphabets
        elif (ord(char) >= 97 and ord(char) <= 122):
            is_small = True

        
        if is_small and is_capital:
            return True
        
    return False

# print(check_alphabet("sass"))


def check_alphnumeric(alphabet) -> bool:
    # check the range that contians alphanumeric characters
    # ASCII
    pass

def check_password(password) -> bool:

    if len(password) >= 8 and check_alphabet(password) and check_alphnumeric(password):
        return True
    
    return False


# Two things a valid email should have?
# .com
# @

# Supporting function
def valid_email(email):
    if '@' in email and '.com' in email:
        return True
    return False


def login(email, password):

    # use of supporting function
    if valid_email(email):
        file = open("signup.txt", "r")  
        has_email = False
        has_password = False

        for line in file:
            if email in line:
                has_email = True
            elif password in line:
                has_password = True
            
        if has_email and has_password:
            return True
    
    return False

# print(login("will.smith@gmail", "will12345"))

def create_post(email, content):
    # use file handing to write the data
    # email
    # content
    # space
    pass




def filter_post(email):
    all_posts = []
    file = open("post.txt", "r")
    for line in file:
        if email in line:
            post = file.readline()            
            all_posts.append(post)
    
    return all_posts

print(filter_post("def@gmail.com"))



# def edit_post(prev_post, new_post):
#     # read the file line by line
#     # find the prev_post
#     # replace the prev_data
#     # with new_post
#     pass

def edit_post(prev_post, new_post):
    file = open("post.txt", "r")
    lines = file.readlines()

    for line in lines:
        if prev_post in line:
            file.write(new_post + '\n')
            
        else:
            file.write(line)
        

edit_post("post", "New york")




# def delete_post(email, prev_post):

#     pass

def delete_post(prev_post, email):
     file = open("post.txt", "r")
     lines = file.readlines()
     for line in lines:
         if email in line and file.readline() == prev_post:
             return email + "" + prev_post

print(delete_post("Lander.sh@gmail.com", "farm"))








def check_alphnumeric(password) -> bool:
        for char in password:
            if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
                return False
        return True