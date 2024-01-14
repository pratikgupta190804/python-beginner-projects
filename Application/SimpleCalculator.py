print("Welcome to my Computer :)")
print("Select an operation. ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")

while True:
   try:
     while True:
       choice = int(input("Enter your choice(1/2/3/4/5): "))
       if choice>=1 and choice<=5:
         break
       else:
         print("Enter between 1 and 5")
     break
   except ValueError:
      print("Please Enter a Number")

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def power(x,y):
    return x**y

if choice == 1:
    print (num1, "+", num2, "=", add(num1,num2))

elif choice == 2:
    print (num1, "-", num2, "=", subtract(num1,num2))

elif choice == 3:
    print (num1, "*", num2, "=", multiply(num1,num2))

elif choice == 4:
    print (num1, "/", num2, "=", divide(num1,num2))

elif choice == 5:
    print ( num1, "**", num2, "=", power(num1,num2))

else:
  print("Invalid input")
  
