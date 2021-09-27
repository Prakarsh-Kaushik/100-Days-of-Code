#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to Bill Splitter \n")
bill = float(input("Enter the bill amount - Rs. "))
tip = int(input("Enter the tip percent (without % sign) - "))
shares = int(input("Enter the number of people to split among - "))

tipPercent = tip / 100
tipAmount = bill * tipPercent
billWithTip = bill + tipAmount

perPerson = billWithTip / shares
finalBill = "{:.2f}".format(perPerson)

print()
print(f"Total bill including tip is Rs. {billWithTip}")
print(f"Each person should pay Rs. {finalBill}")