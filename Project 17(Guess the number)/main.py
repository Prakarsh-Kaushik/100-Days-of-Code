from random import randint
from art import logo
print(logo)

easyTurn = 10
hardTurn = 5



def checkAnswer(guess, answer, turns):
  if guess > answer:
    print("\nToo High")
    return turns-1
  elif guess < answer:
    print("\nToo Low")
    return turns-1
  else:
    print(f"\n Congratulations, You got it. The correct guess was {answer}")

def level():
 difficulty = input("Choose a level of Difficulty. Type 'easy' or 'hard' ? ")
 if difficulty == "easy":
   return easyTurn
 else:
   return hardTurn 

def game():
  print("\nWelcome to Number Guessing Game \n")
  turns = level()
  print("\nI'm thinking of a number between 1 to 100")
  answer = randint(1, 100)

  guess = 0 

  while guess != answer:
    print(f"\nYou've {turns} turns left \n")
    guess = int(input("\nMake a Guess : "))
    turns = checkAnswer(guess, answer, turns)
    print(f"{answer}")
    if turns == 0:
      print("You are out of guesses, You Lose")
      return
    elif guess != answer:
      print("Guess again.")

game()