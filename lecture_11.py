# Exception Handling 
# try:
# except

# try:
#     num = int(input("Enter a number: "))
#     print(24 / num)
# except ZeroDivisionError as e:
#     print('Division by zero is not allowed\nPlase provide the input again')


def take_input(num):
    try:
        print(24 / num)
        print("24" + 12)
    except ZeroDivisionError:
        print('Division by zero is not allowed\nPlase provide the input again')
        take_input(int(input("Enter a number")))
    except TypeError as e:
        print("Type Error. Cannot combine strings with numbers")    
    finally:
        print("Hi there!")

num = int(input("Enter a number: "))    
take_input(num)


# Test Case
# Quality Assurance

