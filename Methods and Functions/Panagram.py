import string

def panagram(str):
  alphabet = string.ascii_lowercase
  str = str.replace(" ","")
  check = False

  for s in alphabet:
    if(s in str):
      check = True
    else:
      break
    
  if(check):
    return "It's a panagram"
  else:
    return "It's not a panagram"
  
result = panagram("The quick brown fox jumps over the lazy dog")
print(result)
result = panagram("hello world")
print(result)

"""def panagram(str):
  alphabet = string.ascii_lowercase
  alphabet = set(alphabet)
  str = str.replace(" ","")
  str = sorted(set(str))

  if(str==alphabet):
    return "It's a panagram"
  else:
    return "It's not a panagram"

result = panagram("The quick brown fox jumps over the lazy dog")
print(result)
result = panagram("hello world")
print(result)"""
