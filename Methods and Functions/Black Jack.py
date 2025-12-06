def black_jack(num1,num2,num3):
  num_list = [num1,num2,num3]
  sum_of_num = sum(num_list)
  reduced_sum = sum_of_num-10

  if(sum_of_num<=21):
    return sum_of_num
  elif(sum_of_num>21 and 11 in num_list):
    return reduced_sum
  elif(reduced_sum>21):
    return "BUST"
  

result = black_jack(5,6,7)
print(result)
result = black_jack(9,9,9)
print(result)
result = black_jack(9,9,11)
print(result)