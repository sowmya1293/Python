def paper_doll(str):
  new_str = ""

  for l in str:
    new_str = new_str+l*3

  return new_str


result = paper_doll("fast")
print(result)
result = paper_doll('Mississippi')
print(result)
