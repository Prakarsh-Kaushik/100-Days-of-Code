from art import logo

def add(n1, n2):
  """ Adds the two number """
  return n1 +  n2

def sub(n1, n2):
  """Subtracts two numbers """
  return n1 - n2

def multiply(n1, n2):
  """ Multiplies two numbers """
  return n1 * n2

def divide(n1, n2):
  """Divides two numbers """

operation = { 
  "+" : add,
  "-" : sub,
  "*" : multiply,
  "/" : divide
  }

def calculator():
  print(logo + "\n \n")
  num1 = float(input("\n Enter the first number - "))
  print()

  for symbol in operation:
    print(symbol)

  toContinue = True

  while toContinue:
    choice = input("\n Choose an operation from the above list - ")
    num2 = float(input("\n Enter the next number - "))

    calculation = operation[choice]
    answer1 = calculation(num1, num2)

    print(f"\n {num1} {choice} {num2} = {answer1}")

    if input("\n Type 'y' to continue with {answer} or type 'n' to start a new calculation - ") == "y":
      num1 = answer1
    else:
      toContinue = False
      clear()
      calculator()

calculator()