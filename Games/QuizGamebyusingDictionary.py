# -------------------------
def new_game():
  choices = ['A', 'B', 'C', 'D']
  guesses = []
  correct_guesses = 0
  score = 0
  question_number = 1
  print("Welcome to the Quiz Game!")
  for keys in questions:
    print("----------------------------")
    print(keys)
    for answer in answers[question_number-1]:
      print(answer)
    while True:
      try:
        user_answer = input("Enter your answer(A/B/C/D): ").upper()
        if user_answer in choices:
          break
        else:
          print("Enter a valid answer")
      except:
          print("Invalid Input")
      
    guesses.append(user_answer)  
    correct_guesses += check_answer(questions.get(keys),user_answer)
    question_number += 1

  display_score(correct_guesses)
# -------------------------
def check_answer(answer,guess):
  if answer == guess:
    print("CORRECT ANSWER!")
    return 1
  else:
    print("WRONG ANSWER!")
    return 0
# -------------------------
def display_score(correct_guesses):
  score = int((correct_guesses/len(questions))*100)
  print("Your score is: ",str(score)," %")

# -------------------------
def play_again():
  response = input("Do you want to play again? (Y/N): ").upper()
  if response == 'Y':
    return True
  else:
    return False

# -------------------------

questions = {
"1.who is the current president of India ?":"B",
"2.What is the name of the landing point of chandrayaan-3 ?":"C",
"3.who is the current President of USA ?":"B",
"4.Who was the first Prime Minister of India?":"A",
"5.Who was the father of Indian space program ?":"A",
"6.Who is the richest man in India ?":"D",
"7.Which is the longest river in India ?":"A",
"8.Who is known as the 'Ironman of India' ?":"A",
"9.Which is the largest desert of India ?":"A",
"10.Which is the national tree of India ?":"C"
}
answers = [
["A.Ram Nath Kovind", "B.Droupadi Murmu", "C.Rajendra Prasad", "D.Pranab Mukherjee"],
[ "A.Jawahar Point", "B.Shiva Point", "C.Shiv Shakti Point", "D.Shakti Point"],
["A.Barack Obama", "B.Joe Biden", "C.Donald Trump", "D.Bill Clinton"],
["A.Jawaharlal Nehru", "B.M.K.Gandhi", "C.Subhash Chandra Bose", "D.Lal Bahadur Shastri"],
["A.Vikram Sarabhai", "B.Homi J. Bhabha","C.A.P.J Abdul Kalam", "D.Satyendranath Bose"],
["A.Gautam Adani", "B.Savitri Jindal", "C.Shiv Nadar", "D.Mukesh Ambani"],
["A.Ganga", "B.Yamuna", "C.Godavri", "D.Brahmaputra"],
["A.Sardar Vallabhbhai Patel", "B.Bhagat Singh", "C.Chandrashekhar Azad", "D.Lal bahadur Shastri"],
["A.Thar desert", "B.Rann of Kutch", "C.Ladakh desert", "D.Cold desert"],
["A.Mango", "b.Peepal", "c.Banyan", "d.Neem"]
]

new_game()

while play_again():
  new_game()

print("Thanks for playing!")
