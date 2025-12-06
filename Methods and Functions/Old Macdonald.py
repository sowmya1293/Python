def old_macdonald(str):
  word = []

  for i in str:
    word.append(i)

  word[0]=word[0].upper()
  word[3] = word[3].upper()
  str = "".join(word)
  return str


result = old_macdonald("macdonald")
print(result)