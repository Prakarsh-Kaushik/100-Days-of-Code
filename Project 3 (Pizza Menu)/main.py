# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

smallPizza = 15
mediumPizza = 20
largePizza = 25


pepperoniSmall = 2
pepperoniMedLar = 3
extraCheese = 1

if size == "S":
  total+= smallPizza
  if add_pepperoni == "Y":
    total+=pepperoniSmall
  if extra_cheese == "Y":
    total+= extraCheese 
elif size == "M":
  total+= mediumPizza
  if add_pepperoni == "Y":
    total+=pepperoniMedLar
  if extra_cheese == "Y":
    total+= extraCheese 
elif size =="L":
  total+= largePizza
  if add_pepperoni == "Y":
    total+=pepperoniMedLar
  if extra_cheese == "Y":
    total+= extraCheese 

print(f"Your final bill is: ${total}")
