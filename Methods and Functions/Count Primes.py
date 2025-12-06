def count_prime(num):
  count = 0

  for num1 in range(2,num+1):
    for num2 in range(2,num1):
      if(num1%num2==0):
        break
    else:
      count=count+1
  return count


result = count_prime(100)
print(result)
