# This is a program for a simple rock, paper, scissors game

import random, sys

print('ROCK PAPER SCISSORS\n')

print('Press (q) anytime to close the game\n')

# These variables keep track of the number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True: #The game will run in this while loop
    print(f' {wins} WINS, {losses} LOSSES, {ties} TIES')
    while True:                                     #PLAYER INPUT
        print('Press (q) to close the game\n')
        player_move = input('Enter your move: (r)ock (p)aper (s)cissors\n')
        if player_move == 'q':
            sys.exit() #Quit the program
        elif player_move == 'r' or player_move == 'p' or player_move == 's':
            break

        print('You have to type a valid input\n')

    # DISPLAY PLAYER'S CHOICE
    if player_move == 'r':
        print('You picked ROCK')
    elif player_move == 'p':
        print('You picked PAPER')
    elif player_move == 's':
        print('You picked SCISSORS')
    
    # DISPLAY COMPUTER'S CHOICE
    computer_number = random.randint(1,3)

    if computer_number == 1:
        computer_move = 'r'
        print('CPU picked ROCK')
    elif computer_number == 2:
        computer_move = 'p'
        print('CPU picked PAPER')
    elif computer_number == 3:
        computer_move = 's'
        print('CPU picked SCISSORS')
    
    # CHECKING WHO WON
    if computer_move == player_move: #TIE SITUATION
        print("It's a tie!")
        ties += 1
    elif computer_move == 'r' and player_move == 'p': #PLAYER WIN SITUATION
        print('You won!')
        wins += 1
    elif computer_move == 'p' and player_move == 's':
        print('You won!')
        wins += 1
    elif computer_move == 's' and player_move == 'r':
        print('You won!')
        wins += 1
    elif computer_move == 'p' and player_move == 'r': #CPU WIN SITUATION
        print('You lost! :(')
        losses += 1
    elif computer_move == 'r' and player_move == 's':
        print('You lost! :(')
        losses += 1
    elif computer_move == 's' and player_move == 'r':
        print('You lost! :(')
        losses += 1