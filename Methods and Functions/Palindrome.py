def palindrome(str):
  str = str.replace(" ","")
  
  reverse_str = str[::-1]

  if(str==reverse_str):
    return True
  else:
    return False
  

result = palindrome('madam')
print(result)
result = palindrome('Hi')
print(result)