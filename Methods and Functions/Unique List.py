def unique_list(listOne):
  listTwo = []

  for i in range(0,len(listOne)):
    if(listOne[i] in listTwo):
      continue
    else:
      listTwo.append(listOne[i])

  return listTwo


result = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(result)