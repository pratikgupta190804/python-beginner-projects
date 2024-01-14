print("Welcome to my Quiz!")

player1=input("Do you want to play? yes or no- ")
if player1.lower() not in ["yes","y"]:
    quit()
  
print("Okay! Lets play :)")
score = 0

print("1.who is the current president of India ?")
print("a.Ram Nath Kovind")
print("b.Droupadi Murmu")
print("c.Rajendra Prasad")
print("d.Pranab Mukherjee")

answer=input("Enter your choice a/b/c/d - ")

if answer.lower() == "b":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: 
      print("""Incorrect answer :(
Do you best on another question :)""")
    
print("2.What is the name of the landing point of  chandrayaan-3 ?")
print("a.Jawahar Point")
print("b.Shiva Point")
print("c.Shiv Shakti Point")
print("d.Shakti Point")

answer=input("Enter your choice a/b/c/d - ")
    
if answer =="c":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("3.who is the current President of USA ?")
print("a.Barack Obama")
print("b.Joe Biden")
print("c.Donald Trump")
print("d.Bill Clinton")

answer=input("Enter your choice a/b/c/d - ")

if answer =="b":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("4.Who was the first Prime Minister of India?")
print("a.Jawaharlal Nehru")
print("b.M.K.Gandhi")
print("c.Subhash Chandra Bose")
print("d.Lal Bahadur Shastri")

answer=input("Enter your choice a/b/c/d - ")

if answer =="a":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("5.Who was the father of Indian space program ?")
print("a.Vikram Sarabhai")
print("b.Homi J. Bhabha")
print("c.A.P.J Abdul Kalam")
print("d.Satyendranath Bose")

answer=input("Enter your choice a/b/c/d - ")
    
if answer =="a":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("6.Who is the richest man in India ?")
print("a.Gautam Adani")
print("b.Savitri Jindal")
print("c.Shiv Nadar")
print("d.Mukesh Ambani")

answer=input("Enter your choice a/b/c/d - ")

if answer =="d":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("7.Which is the longest river in India ?")
print("a.Ganga")
print("b.Yamuna")
print("c.Godavri")
print("d.Brahmaputra")

answer=input("Enter your choice a/b/c/d - ")
    
if answer =="a":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("8.Who is known as the 'Ironman of India' ?")
print("a.Sardar Vallabhbhai Patel")
print("b.Bhagat Singh")
print("c.Chandrashekhar Azad")
print("d.Lal bahadur Shastri ")

answer=input("Enter your choice a/b/c/d - ")
    
if answer =="a":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("9.Which is the largest desert of India ?")
print("a.Thar desert")
print("b.Rann of Kutch")
print("c.Ladakh desert")
print("d.Cold desert")

answer=input("Enter your choice a/b/c/d - ")
    
if answer =="a":
  print("Correct answer!")
  score += 1
  print("Lets get to another question:)")
else: print("""Incorrect answer :(
Do you best on another question :)""")

print("10.Which is the national tree of India ?")
print("a.Mango")
print("b.Peepal")
print("c.Banyan")
print("d.Neem")

answer=input("Enter your choice a/b/c/d - ")
    
if answer =="c":
  print("Correct answer!")
  score += 1
else: print("Incorrect answer :( ")

print("You got " + str(score) + " questions correct. ")
print("You got " + str((score / 10) * 100) + "% in this test. " )
