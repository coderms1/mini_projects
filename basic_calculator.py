#basic_calculator.py

"""
This is a basic calculator where you punch in 
two numbers and pick what you want to do—add, 
subtract, multiply, or divide. It gives you 
the answer right away, unless you try to divide 
by zero (then it calls you out). 
Quick and easy math without needing a real calculator!
"""

iNum1 = float(input("Enter a number: "))
iNum2 = float(input("Enter another number: "))
sOperation = input("Enter an operation (+ - * /): ")

if sOperation == "+":
  answer = iNum1 + iNum2
  print(f"The answer to your problem is: {answer}")
elif sOperation == "-":
  answer = iNum1 - iNum2
  print(f"The answer to your problem is: {answer}")
elif sOperation == "*":
  answer = iNum1 * iNum2
  print(f"The answer to your problem is: {answer}")
elif sOperation == "/":
    if iNum2 != 0:
      answer = iNum1 // iNum2 
      print(f"The answer to your problem is: {answer}")
    else:
      print("Cannot divide by zero.")
else:
  ("Invalid operation, try again.")

