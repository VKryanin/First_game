import random

game_status = True
while game_status:
    player_choice = input('Player choice: [paper/rock/scissors] \n').lower()
    if player_choice not in ['paper', 'rock', 'scissors']:
        print('Incorrect input. Try again')
        continue
    gen = {1:'paper', 2:'rock', 3:'scissors'}
    comp_choice = gen[random.randint(1,3)]
    print(f'Comp choice = {comp_choice}')
    win_comb = [('paper', 'rock'), ('rock', 'scissors'),('scissors', 'paper')]
    if player_choice == comp_choice:
        print('A draw')
    elif (player_choice, comp_choice) in win_comb:
        print('Player wins')
    else:
        print('Comp wins')
    game_status = input('Do you want priceed? [Yes/No]').lower() == 'yes'
