#Print multiplication table of a given number



def showMultiplicationTable():
    num = int(input("Enter a number"))

    for i in range(1,11):
        print(num*i)



showMultiplicationTable()