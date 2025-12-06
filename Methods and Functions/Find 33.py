def find_adjacent_num(num_list):
  for i in range(0,len(num_list)):
    if(num_list[i]==3):
      if(num_list[i+1]==3):
        return True
      elif(num_list[i+1]==None):
        return False
      else:
        return False
      

result = find_adjacent_num([1, 3, 3])
print(result)
result = find_adjacent_num([1, 3, 1, 3])
print(result)
result = find_adjacent_num([3, 1, 3])
print(result)
  