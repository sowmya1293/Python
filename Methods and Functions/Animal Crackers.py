def animal_crackers(str1,str2):
  words = []

  words.append(str1)
  words.append(str2)

  if(words[0][0]==words[1][0]):
    return True
  else:
    return False
  

result = animal_crackers("Levelheaded","Llama")
print(result)
result = animal_crackers("Crazy","Kangaroo")
print(result)