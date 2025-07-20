#Display Fibonacci series up to 10 terms


def displayFibonacci():
    firstNum = 0
    secondNum = 1

    for i in range(8):
        thirdNum = firstNum+secondNum
        print(thirdNum)
        firstNum = secondNum
        secondNum = thirdNum


displayFibonacci()