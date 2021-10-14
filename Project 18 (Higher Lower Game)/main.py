import random 
from art import logo, vs
from game_data import data
from replit import clear

def printData(account):
  """Format game data into readble form"""
  accountName = account["name"]
  accountDescription = account["description"]
  accountCountry = account["country"]

  return f"{accountName} is a {accountDescription}. {accountName} is from {accountCountry}"

def checkGuess(userGuess, accountFollowerA, accountFollowerB):
  if accountFollowerA > accountFollowerB:
    return userGuess == "a"
  else:
    return userGuess == "b"

#Display Start art 
print(logo)

score = 0
continueGame = True
accountB = random.choice(data)

while continueGame:
  #Generate Random Acc from game data
  accountA = accountB
  accountB = random.choice(data)

  while accountA == accountB :
    accountB = random.choice(data)

  print(f"\nCompare A : {printData(accountA)} \n {vs} \nCompare B : {printData(accountB)}")

  #ask user for guess
  userGuess = input("\nWho has more follower's ? Type 'A' or 'B' : ").lower()

  #check guess right or wrong
  ## get follower from each acc
  accountFollowerA = accountA["follower_count"]
  accountFollowerB = accountB["follower_count"]

  ## check using if its correct
  correctGuess = checkGuess(userGuess, accountFollowerA, accountFollowerB)

  clear()
  print(logo)

  #display right or wrong
  if correctGuess:
    score+=1
    print(f"\nYou're Right.\nYour score is {score}")
  else:
    continueGame = False
    print(f"\nYou're Wrong\nYour final score is {score}")



