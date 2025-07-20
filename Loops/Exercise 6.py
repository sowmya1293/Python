#Count the total number of digits in a number

def countDigits(num):
    num = str(num)
    count = 0

    for n in num:
        count += 1
    print(count)

countDigits(75869)



#adding induvidual digits of a given number
"""def countTheDigits(num):
    strNum = str(num)
    divisor = "1"
    sum = 0
    i = 0

    while i<len(strNum):
        divisor = divisor+"0"
        i+=1

    divisor = int(divisor)

    while(divisor>=10):
        sum = sum+math.floor((num/divisor))
        num = num%divisor
        divisor = divisor/10
    sum = sum+int(num)

    print(sum)


countTheDigits(75869)"""

    