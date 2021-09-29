# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinedName = name1 + name2
lowerCase = combinedName.lower()

t = lowerCase.count("t")
r = lowerCase.count("r")
u = lowerCase.count("u")
e = lowerCase.count("e")

true = t+r+u+e

l = lowerCase.count("l")
o = lowerCase.count("o")
v = lowerCase.count("v")
e = lowerCase.count("e")

love = l+o+v+e

love_score = str(true)+str(love)
score = int(love_score)

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else :
  print(f"Your score is {score}.")