#given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

import math

def printReverse(num):
    numString = str(num)
    lenOfStr = len(numString)
    quotient = []
    divisor = "1"
    
    for i in range(lenOfStr-1):
        divisor = divisor+"0"
    divisor = int(divisor)

    while(divisor!=1):
        q = math.floor(num/divisor)
        quotient.append(q)
        num = num%divisor
        divisor = divisor/10
    quotient.append(int(num))

    quotient = quotient[::-1]
    print(quotient)


printReverse(7536)














"""quotientOne = math.floor(num/1000) #7
    reminderOne = num%1000 # 356

    quotientTwo = math.floor(reminderOne/100) #3
    reminderTwo = reminderOne%100 #56

    quotientThree = math.floor(reminderTwo/10) #5
    reminderThree = reminderTwo%10 #6

    print(reminderThree,quotientThree,quotientTwo,quotientOne)


printReverse(7356)"""