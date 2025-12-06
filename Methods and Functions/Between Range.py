def range(num,low,high):
  if(low<num<high):
    return f"{num} is between {low} and {high}"
  else:
    return f"{num} not in range"
  

result = range(5,2,7)
print(result)
result = range(3,1,10)
print(result)