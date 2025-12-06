def makes_twenty(num1,num2):
  if(num1+num2==20):
    return True
  elif(num1==20 or num2==20):
    return True
  else:
    return False
  

result = makes_twenty(20,10)
print(result)
result = makes_twenty(2,3)
print(result)