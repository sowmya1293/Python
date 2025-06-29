#Write a code to return True if the list’s first and last numbers 
#are the same. If the numbers are different, return False.

def checkValues(inputList):
    lastValue = len(inputList)-1

    if(inputList[0]==inputList[lastValue]):
        return True
    else:
        return False
    

result=checkValues([75, 65, 35, 75, 30])
print(result)
#checkValues([75, 65, 35, 75, 30])
