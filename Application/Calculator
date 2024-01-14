import math

def add(x,y):
  return x+y
  
def subtract(x,y):
  return x-y
  
def multiply(x,y):
  return x*y
  
def divide(x,y):
  return x/y
  
def squareroot(x):
  return x^(1/2)
  
def factorial(x):
  return math.factorial(x)

def sin(x):
  return math.sin(x)

def cos(x):
  return math.cos(x)

def tan(x):
  return math.tan(x)

def sinh(x):
  return math.sinh(x)

def cosh(x):
  return math.cosh(x)

def tanh(x):
  return math.tanh(x)

def log(x):
  return math.log10(x)


print("Welcome To Mycalculator:) ")
print("Select an operator. ")

print("1.Add    2.Subtract    3.Multiply\n4.Divide 5.Square Root 6.Factorial\n7.sin    8.cos         9.tan\n10.sinh 11.cosh       12.tanh\n13.log base 10")

while True:
  try:
    choice = int(input("Enter your choice(1/2/3/4/5/6/7/8/9/10/11/12/13): "))
    if choice > 13 or choice < 1:
      print("Invalid choice. Try again.")
      continue
    break
  
  except:
    print("Invalid choice. Try again.")
    continue


if choice in range(5):
  x = float(input("Enter the first number: "))
  y = float(input("Enter the second number: "))
  if choice == 1:
    print(x , "+", y, "=", add(x,y))
  elif choice == 2:
    print(x , "-", y, "=", subtract(x,y))
  elif choice == 3:
    print(x , "X", y, "=", multiply(x,y))
  elif choice == 4:
    print(x , "/", y, "=", divide(x,y))

elif choice in range(5,14):
  x = float(input("Enter value of x : "))
  if choice in range(7,13):
    x = math.radians(x)
  if choice == 5:
    print("√",x , "=", squareroot(x))
  elif choice == 6:
    print(x , "!", "=", factorial(x))
  elif choice == 7:
    print("sin", x , "=", sin(x))
  elif choice == 8:
    print("cos", x , "=", cos(x))
  elif choice == 9:
    print("tan", x , "=", tan(x))
  elif choice == 10:
    print("sinh", x , "=", sinh(x))
  elif choice == 11:
    print("cosh", x , "=", cosh(x))
  elif choice == 12:
    print("tanh", x , "=", tanh(x))
  elif choice == 13:
    print("log ",x , "=", log(x))
