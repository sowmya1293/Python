#Capitalize the first letter of each word in a string

def capitalize_words(text):
  
  words = text.split()  # Split the string into a list of words
  capitalized_words = [word.capitalize() for word in words]  # .captialize() capitalizes the first letter of a word
  return " ".join(capitalized_words)  # Join the capitalized words back into a string

# Get input from the user
str1 = "pynative.com is for python lovers"

capitalized_string = capitalize_words(str1)
print("Capitalized string:", capitalized_string)