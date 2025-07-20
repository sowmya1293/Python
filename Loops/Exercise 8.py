#Print list in reverse order using a loop


def printInReverse(input):
    length = len(input)

    for i in range(length-1,-1,-1):
        print(input[i])


printInReverse([10, 20, 30, 40, 50])