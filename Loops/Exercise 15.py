# Print elements from a given list present at odd index positions


def printElements(myList):
    endIndex = len(myList)

    for i in range(1,endIndex,2):
        print(myList[i])

printElements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])