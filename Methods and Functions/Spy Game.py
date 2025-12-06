def spy_game(num_list):
  num1 = 0
  num2 = 7
  list_of_nums = []

  if((num1 not in num_list) or (num2 not in num_list) or (num_list.index(num1)>num_list.index(num2))):
    return False
  else:
    index_one = num_list.index(0)
    list_of_nums = num_list[index_one+1:]

    if(num1 not in list_of_nums):
      return False
    else:
      index_two = list_of_nums.index(0)
      index_three = list_of_nums.index(7)

      if(index_two<index_three):
        return True
      else:
        return False
      

result = spy_game([1,2,4,0,0,7,5])
print(result)
result = spy_game([1,0,2,4,0,5,7])
print(result)
result = spy_game([1,7,2,0,4,5,0])
print(result)
  

