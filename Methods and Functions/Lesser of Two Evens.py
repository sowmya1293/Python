def lesser_of_two_evens(num1,num2):
  if(num1%2==0 and num2%2==0):
    return min(num1,num2)
  else:
    return max(num1,num2)
  

num = lesser_of_two_evens(2,4)
print(num)
num = lesser_of_two_evens(2,5)
print(num)
    