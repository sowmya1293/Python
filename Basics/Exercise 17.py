#Generate Fibonacci series up to 15 terms

def fibonacci():
    i=0
    firstNum = 0
    secondNum = 1

    print(firstNum,end=" ")
    while(i<13):
        nextNum = firstNum+secondNum
        print(nextNum,end=" ")
        firstNum = secondNum
        secondNum = nextNum
        i+=1


fibonacci()