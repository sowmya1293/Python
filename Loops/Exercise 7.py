#Write a Python program to print the reverse number pattern using a for loop.
"""5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1"""

def printPattern():
    for i in range(5,0,-1):
        print('\n')
        for j in range(i,0,-1):
            print(j,end=" ")


printPattern()