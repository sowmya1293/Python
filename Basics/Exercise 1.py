#Given two integer numbers, write a Python program to return their product
#only if the product is equal to or lower than 1000. Otherwise, return their sum.

def sumAndProduct(a,b):
    prod = a*b
    if(prod<=1000):
        return prod
    else:
        return a+b
    
resultOne = sumAndProduct(20,30)
print(resultOne)
resultTwo = sumAndProduct(40,30)
print(resultTwo)