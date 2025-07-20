#Reverse a integer number



def reverseNum(num):
    reversedStr = ""
    num = str(num)
    length = len(num)

    for i in range(length-1,-1,-1):
        #print(i)
        reversedStr = reversedStr+num[i]
    print(reversedStr)

reverseNum(76542)