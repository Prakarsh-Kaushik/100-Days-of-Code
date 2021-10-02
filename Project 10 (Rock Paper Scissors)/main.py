import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

outcomeImages = [rock, paper, scissors]

userChoice = int(input("What do you choose ? \n Type 0 for Rock, 1 for Paper & 2 for Scissor. \n")
)

if userChoice >= 3 or userChoice < 0:
  print("Enter a valid number, You lose.")
else:
  print("User chose - ")
  print(outcomeImages[userChoice])


  computerChoice = random.randint(0,2)

  print("Computer chose - ")
  print(outcomeImages[computerChoice])

  if userChoice == 0 and computerChoice == 2:
    print("You win")
  elif userChoice == 2 and computerChoice == 0:
    print("You lose")
  elif userChoice > computerChoice:
    print("You win")
  elif userChoice < computerChoice:
    print("You lose")
  elif userChoice == computerChoice:
    print("It's a draw, Play Again !!! ")
