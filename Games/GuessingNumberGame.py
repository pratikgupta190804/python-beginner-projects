import random

player1 = input("Do you want to play? yes or no - ")

if player1.lower() != "yes" :
  quit()

else:
  print("Select range you want to guess ")

x = int(input("Type a player1ing number: "))
if x < 0:
    print("Please type larger number than 0 next time.")
    quit()
  
y = int(input("Type a ending number: "))
if y < 0:
    print("Please type larger number than 0 next time.")
    quit()

while True:
   try:  
     while True:
       guess = int(input("Guess your number: "))
       if guess>x and guess<y:
         break
       else:
         print(f"Enter a number between {x} and {y}")
     break
   except ValueError:
      print("Please Enter a Number")
range = random.randint(x,y)
print(range)

if guess == range:
  print("Correct Guess :)")
else:
  print("Bad Luck :(" )
  print("Better Luck next time ")

