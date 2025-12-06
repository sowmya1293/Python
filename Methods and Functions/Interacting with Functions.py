#Guess where the hidden 'O' is
from random import shuffle

mixedup_list = []

def shuffle_list(myList):
  shuffle(myList)
  return myList

def player_guess():
  guess = ''
  
  while guess not in ['0','1','2']:
    guess = input("Pick a number between 0 to 2")
  print(int(guess))
  return int(guess)

def check_guess(myList,guess):
  if(myList[guess] == 'O'):
    print("Correct!")
  else:
    print("Wrong guess")
    print(myList)


myList = ['', 'O', '']
mixedup_list = shuffle_list(myList)
guessed_number = player_guess()
check_guess(mixedup_list, guessed_number)