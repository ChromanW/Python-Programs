# Strings
# list of characters
fruit = "Mango"
# fruit = ['M', 'a', 'n', 'g', 'o']

# Attributes

# Concatenation
# combine multiple strings together

firstName = "Sam"
lastName = "Smith"
fullName = firstName + " " + lastName
print(fullName)

# Multplication
print("@" * 20)

# Indexing
# positioning
# Always starts from 0
# index : value
print(fruit[3])

# Slicing/Substring
# Divide original string into smaller chunks
# start Index : end index
sentence = "we are lEarning pYtHon"
print(sentence[7:15])

# Positive Indexing -> 0
# go from left to right

# Negative Indexing -> -1
# go from right to left
print(sentence[:-6])


# Funtions

# Length
# provides you the length of a string
print(len(sentence))

# Upper
print(sentence.upper())
# Lower
print(sentence.lower())
# Capitalize
print(sentence.capitalize())

# Count
print(sentence.count('a'))

# in operator
print('pYtHon' in sentence)

# strip()
# leading and trailing whitespace
name = input("Enter your name: ")
name = name.strip()
print(name)