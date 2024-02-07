n_1 = "1"
n_2 = "2"
n_3 = "3"
n_4 = "4"
n_5 = "5"
n_6 = "6"
n_7 = "7"
n_8 = "8"
n_9 = "9"

def print_table():
    print(f'''
       {n_1}   |   {n_2}   |   {n_3}\n
    ------- ------- ------\n
       {n_4}   |   {n_5}   |   {n_6}\n
    ------- ------- ------\n
       {n_7}   |   {n_8}   |   {n_9}
    ''')

print_table()
print("Game starts with X\n")

player1_has_answered = False
player2_has_answered = False
game_number = 0
alreay_used_place = []   

while(game_number < 9):
    player1 = int(input("Enter the place number: "))
    
    if(not player1_has_answered):
        if (player1 in range(1,10)) and (player1 not in alreay_used_place):
            globals()[f'n_{player1}'] = "X"
            alreay_used_place.append(player1)
            player1_has_answered = True
            player2_has_answered = False
            game_number = game_number + 1
        else:
            print("Place is already occupied OR Place out of board. Please choose another place")
    
    print_table()

    if game_number == 9:
        break

    player2 = int(input("Enter the place number: "))
    if(not player2_has_answered):
        if (player2 in range(1,10)) and (player2 not in alreay_used_place):
            globals()[f'n_{player2}'] = "0"
            alreay_used_place.append(player2)
            player2_has_answered = True
            player1_has_answered = False
            game_number = game_number + 1
        else:
            print("Place is already occupied OR Place out of board. Please choose another place")

    print_table()

print("Game Over!")
