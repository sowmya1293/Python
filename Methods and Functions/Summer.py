def summer(num_list):
  num_to_check = 6
  list_one = []
  list_two = []

  if num_to_check not in num_list:
    return sum(num_list)
  else:
    index_one = num_list.index(6)
    index_two = num_list.index(9)+1

    if(index_one==0):
      list_one = num_list[index_two:]
      return sum(list_one)
    else:
      list_one = num_list[0:index_one]
      list_two = num_list[index_two:]
      list_one.extend(list_two)
      #print(list_one)
      return sum(list_one)
    

result = summer([1, 3, 5])
print(result)
result = summer([4, 5, 6, 7, 8, 9])
print(result)
result = summer([2, 1, 6, 9, 11])
print(result)
  