# Calculator functions
from art import logo
# Addition
def add(n1,n2):
  return n1 + n2

# Subtraction
def subtract(n1,n2):
  return n1 - n2

# multiplication
def multiply(n1,n2):
  return n1 * n2

# Division
def divide(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(logo)

  num1 = float(input("What is the first number?: "))

  for operator in operations:
    print (operator)

  should_continue = True
  while should_continue == True:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What is the second number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' if you would like to continue with {answer}, or type 'n' to start a new calculation ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
