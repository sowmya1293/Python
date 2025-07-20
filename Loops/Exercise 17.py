# Find the sum of a series of a number up to n terms



def findSum(num,terms):
    i = 0
    sum = 0
    addChar = str(num)

    while(i<terms):
        sum = sum+num
        temp = str(num)
        temp = temp+addChar
        #print(num)
        num = int(temp)
        i+=1
    print(sum)

findSum(2,5)