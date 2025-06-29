#Write Python code to iterate through the first 10 numbers 
#and, in each iteration, print the sum of the current and previous number.

def SumOfCurrAndPrev():
    prevNum = 0

    for i in range(10):
        sum = prevNum+i
        print("The sum is",sum)
        prevNum = i


SumOfCurrAndPrev()