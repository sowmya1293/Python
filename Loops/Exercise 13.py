# Find the factorial of a given number


def factorial(num):
    fact = 1

    while(num>=1):
        fact = fact*num
        num -= 1
    print(fact)


factorial(5)