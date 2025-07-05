#Print a downward half-pyramid pattern of stars

def printStars():
    for i in range(5,0,-1):
        print("\n")
        for j in range(i,0,-1):
            print("*",end=" ")


printStars()