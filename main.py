import random

user_choice=input('Make a choice: rock or paper, scissors. ').lower()
possible_actions = (['rock', 'paper', 'scissors'])
text=["Let's", 'go', 'ok', '+', 'да','го', 'yes']
he_says_no=['no', 'good buy', 'nope', '-', 'stop','over']
while True:
    computer_choice = random.choice(possible_actions)
    print(computer_choice)
    if user_choice == computer_choice:
        play_again=input('Draw, come on again? ').lower()
        if play_again in he_says_no:
            print('Good buy pussy')
            break
        elif play_again not in text:
            break
        else:
            user_choise = input('Come on one, two, three: ')
            continue
    elif user_choice == 'rock':
        if computer_choice=='paper':
            play_again=input('I won, the paper covers the stone. Do you want to win back the loser? ')
            if play_again in he_says_no:
                print('Good buy pussy')
                break
            elif play_again not in text:
                break
            else:
                user_choice = input('Come on one, two, three: ')
                continue
        else:
            play_again=input('Random chose scissors, you win. Do you want to play some more? I have to win back! ')
            if play_again in he_says_no:
                print('Good buy pussy')
                break
            elif play_again not in text:
                break
            else:
                user_choice = input('Come on one, two, three: ')
                continue
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            play_again=input('Random chose rock, you win. Do you want to play some more? I have to win back ')
            if play_again in he_says_no:
                print('Good buy pussy')
                break
            elif play_again not in text:
                break
            else:
                user_choice = input('Come on one, two, three: ')
                continue
        else:
            play_again=input('I won, scissors cut paper. Let\'s do it again, maybe you\'re lucky?? ')
            if play_again in he_says_no:
                print('Good buy pussy')
                break
            elif play_again not in text:
                break
            else:
                user_choise = input('Come on one, two, three: ')
                continue
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            play_again=input('Random chose paper, you win. Do you want to play some more? I have to win back ')
            if play_again in he_says_no:
                print('Good buy pussy')
                break
            elif play_again not in text:
                break
            else:
                user_choice = input('Come on one, two, three: ')
                continue
        else:
            play_again=input('I won, stone breaks scissors. Do you want to win back? ')
            if play_again in he_says_no:
                print('Good buy pussy')
                break
            elif play_again not in text:
                break
            else:
                user_choice = input('Come on one, two, three: ')
                continue
    play_again=input('Do you know the rules?? Try again) ')
    if play_again in he_says_no:
        print('Good buy pussy')
        break
    elif play_again not in text:
        print('See you soon')
        break

    else:
        user_choice = input('Come on one, two, three: ')
        continue