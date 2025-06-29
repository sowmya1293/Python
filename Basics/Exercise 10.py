#Given two lists of numbers, write Python code to create a new list
#containing odd numbers from the first list and even numbers from the second list.

def mergeLists(listOne,listTwo):
    finalList = []

    for num in listOne:
        if(num%2!=0):
            finalList.append(num)

    for num in listTwo:
        if(num%2==0):
            finalList.append(num)

    print(finalList)


mergeLists([10, 20, 25, 30, 35],[40, 45, 60, 75, 90])