def almost_there(num):
  lower_bound_one = 90
  upper_bound_one = 110
  lower_bound_two = 190
  upper_bound_two = 210
  
  if((num>=lower_bound_one and num<=upper_bound_one) or (num>=lower_bound_two and num<=upper_bound_two)):
    return True
  else:
    return False 
  

result = almost_there(90)
print(result)
result = almost_there(104)
print(result)
result = almost_there(150)
print(result)
result = almost_there(209)
print(result)