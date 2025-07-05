# Print Reverse Number Pattern

def printReverse():
    k=1

    for i in range(5,0,-1):
        print("\n")
        for j in range(1,i+1):
            print(k,end=" ")
        k+=1

printReverse()