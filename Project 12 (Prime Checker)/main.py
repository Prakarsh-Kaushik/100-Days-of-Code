#Write your code below this line ๐
def prime_checker(number):
  isPrime = True
  for num in range(2, number):
   if number%num ==0:
     isPrime = False

  if isPrime:
    print(f"{number} is Prime.")
  else:
    print(f"{number} is Not Prime.")

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



