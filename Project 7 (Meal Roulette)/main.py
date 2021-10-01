import random 
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
inputCount = len(names)

randomName = round(random.random()*inputCount)


pickedName = names[randomName]

print(f"{pickedName} is going to buy the meal today!")

