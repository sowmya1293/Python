#Define a function called myfunc that takes in a string, 
#and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. 


def myfunc(str):
    new_str = ""
    
    for i in range(0,len(str)):
        if (i%2 == 0):
            new_str = new_str+str[i].upper()
        else:
            new_str = new_str+str[i].lower()
    return new_str


result = myfunc("Saturday")
print(result)