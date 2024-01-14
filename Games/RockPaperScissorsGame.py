import random

choices = ["rock", "paper", "scissors"]

ready= input("Are you ready to play?(y or n):  ")

if ready in ["y", "Y"]:
    print("Great! Let's play!")
    
else:
  quit()

while True:
  try:
    player = input("Choose rock, paper, or scissors:  ").lower()
    if player in choices:
      break
    else:
      print("That's not a valid choice.")

  except:
    print(f"{player} is not a valid choice.")

computer_choice = random.choice(choices)
print("Computer: ",computer_choice)
print("player: ",player)

if player == computer_choice:
  print("That's a Tie!")

elif player == "rock":
  if computer_choice == "paper":
    print("You lose!")
  else:
    print("You won!")

elif player == "paper":
  if computer_choice == "scissors":
    print("You lose!")
  else:
    print("You won!")

elif player == "scissors":
  if computer_choice == "rock":
    print("You lose!")
  else:
    print("You won!")

