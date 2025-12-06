def reverse_string(str):
  list_str = str.split(" ")
  list_str.reverse()
  str = " ".join(list_str)

  return str



result = reverse_string("I am home")
print(result)