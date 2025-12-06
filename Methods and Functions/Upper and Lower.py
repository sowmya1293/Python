def upper_and_lower(str):
  count_upper = 0
  count_lower = 0

  for s in str:
    if(s.isupper()):
      count_upper = count_upper+1
    elif(s.islower()):
      count_lower = count_lower+1
    else:
      continue
  return f"no: upper character are {count_upper} and no: lower characters are {count_lower}"


result = upper_and_lower("Hello Mr. Rogers, how are you this fine Tuesday?")
print(result)