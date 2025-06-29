#Write a Python code to accept a string 
#from the user and display characters present at an even index number.

def printEven():
    str = input("Enter the string")
    length = len(str)
    i=0

    while i<length:
        print(str[i])
        i+=2

printEven()