#Check Palindrome Number

def checkPalindrome(num):
    reverseNum = str(num)
    reverseNum = int(reverseNum[::-1])

    if(num==reverseNum):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


checkPalindrome(5005)