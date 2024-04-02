#Read a text file containing word-definition pairs (one pair per line). Create a dictionary where each word is a key and its definition is the value. Then, prompt the user for a word and print its definition from the dictionary (handle non-existent words gracefully).
#cool Means okay
#rizz Definition of charm


#Generate a random number between 1 and 10 (inclusive) and ask the user to guess the number. Provide feedback to the user if their guess is correct or not.

#Define a Python function called is_prime that takes an integer as a parameter and returns True if it's a prime number, and False otherwise. Test the function with the number 13.

#Create a text file named "numbers.txt" with the numbers 1 to 10 each on a new line. Read the file, sum the numbers, and print the result

#Implement a function named generate_password that generates a random password of length 8, consisting of letters (both uppercase and lowercase) and digits.


#--------1.

def create_dictionary(file):
    word_dict = {}
    file = open(file, "r")
    for line in file:
        print(line)
        line = line.strip()
        if line:
            word, definition = line.split(' ', 1)
            word_dict[word] = definition
    return word_dict

def main():
    file_path = 'file_path.txt'
    word_dict = create_dictionary(file_path)
    print(word_dict)
    # while True:
    #     user_input = input("Enter a word (or 'exit' to quit): ").lower()
        
    #     if user_input == 'exit':
    #         break

    #     definition = word_dict.get(user_input, "Word cant be found.")
    #     print(f"Definition: {definition}")

# if __name__ == "__main__":
main()

#--------2. 
import random

Rando_number = random.randint(1, 10)

user = int(input("attempt to guess thee number between 1 and 10: "))

if user == Rando_number:
    print("Your guess is correct.")
else:
    print("You answerd inccorrectly, the correct answer is {7}.")

#-------3.
def is_prime(number):
    if number <= 1:
        return False 
  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  

    return True  

result = is_prime(13)

print(f"Is 13 a prime number {result}")
    
    

#---------4. 
with open('numbers.txt', 'w') as file:
    for number in range(1, 11):
        file.write(str(number) + '\n')

file_path = 'numbers.txt'
total_sum = 0

with open(file_path, 'r') as file:
    for line in file:
        total_sum += int(line.strip())

print(f"The sum of numbers in '{file_path}' is: {total_sum}")

#------5.
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(8))

    return password

generated_password = generate_password()
print("Generated Password:", generated_password)


