#Display numbers from a list using a loop

def displayNum(listOfNum):
    newList = []

    for num in listOfNum:
        if(num%5==0):
            if(num>150):
                if(num>500):
                    break
                else:
                    continue
            newList.append(num)

    print(newList)


displayNum([12, 75, 150, 180, 145, 525, 50])
    