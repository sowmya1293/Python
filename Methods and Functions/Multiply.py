def multiply(list_nums):
  num = 1

  for l in list_nums:
    num = num*l

  return num


result = multiply([1,2,3,-4])
print(result)