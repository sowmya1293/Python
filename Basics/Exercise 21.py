#Check if a user-entered string contains any digits using a for loop

def checkNum(str):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    for i in str:
        if i in numbers:
            return True
    return False


#result = checkNum("Pynative123Python")
result = checkNum("PYnative")
if(result):
    print("The string contains atleast one number")
else:
    print("The string doesn't contain any number")