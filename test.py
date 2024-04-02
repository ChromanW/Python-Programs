def delete_post(prev_post, email):
     file = open("post.txt", "r")
     lines = file.readlines()
     for line in lines:
         if email in line:
             post = file.readline()
             if prev_post == post: 
                return email + "" + prev_post

print(delete_post("Lander.sh@gmail.com", "farm"))