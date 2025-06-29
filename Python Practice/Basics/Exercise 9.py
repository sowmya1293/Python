#Write a Python code to check if the given number is a palindrome.

def palindrome(num):
    num = str(num)

    if(num[::-1]==num):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


palindrome(121)
palindrome(125)
