#Write a Python code to find how often the substring “Emma” appears in the given string.

def numberOfOccurences(str,name):
    count = 0
    listOfStrings = str.split(" ")

    for s in listOfStrings:
        if(s==name):
            count += 1
    print(count)

 

numberOfOccurences("Emma is good developer. Emma is a writer","Emma")