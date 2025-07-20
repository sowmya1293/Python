#Write a program to print the following start pattern using the for loop
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


def printPattern():
    for i in range(0,6):
        if(i>=5):
            for i in range(4,0,-1):
                print('\n')
                for j in range(0,i):
                    print('*',end=" ")
        else:
            print('\n')
            for j in range(0,i+1):
                print('*',end=" ")


printPattern()