#Write a Python code to display numbers from a list divisible by 5

def divisibleByFive(inputList):
    for num in inputList:
        if(num%5==0):
            print(num)


divisibleByFive([10, 20, 33, 46, 55])