# This is a program for a Tic Tac Toe game
#It's important to use the numpy library to make use of 2D arrays
#This is a game for 2 players
import numpy as np
import sys

#These variables keep track of the number of wins, losses and ties
wins_p1 = 0
wins_p2 = 0
ties = 0

#Creating a matrix to represent the grid

grid = np.zeros((3,3), dtype=int)

#A VARIABLE TO RESET THE GAME (yes a needed that to reset the the first loop and restart the game)

end_game = False

#FUNCTIONS
def print_grid():
    #This function exists only to translate and print the '0's, '1's and '2's into ' 's, 'O's and 'X's
    for i in range(3):
        for j in range(3):
            if j == 2:
                #This is what happens when the code prints a item on the last column, so it skips to the next line of the grid          
                if grid[i, j] == 0:
                    print('  ')
                elif grid[i, j] == 1:
                    print(' O')
                elif grid[i, j] == 2:
                    print(' X')
            else:
                #This is the situation when there's still more content on the grid line, not skipping to the next line
                if grid[i, j] == 0:
                    print('   |', end=" "),
                elif grid[i, j] == 1:
                    print(' O |', end= " "),
                elif grid[i, j] == 2:
                    print(' X |', end= " "),

def print_info():
    #Just print some information about grid elements positioning
    print (' 7 | 8 | 9 ')
    print (' 4 | 5 | 6 ')
    print (' 1 | 2 | 3 ')

def apply_on_grid(number, choice):
    #This function only serves to apply the user's choice in the correct position of the grid 
    for i in range(3):
        if choice/3 <= i+1: #Checks if the player number of choice belongs to the bottom, middle or top line (following this respective sequence)
            if choice % 3 == 1:
                if grid[(2-i), 0] != 0:
                    print('You can not place here! >:(')
                    continue
                else:
                    grid[(2-i), 0] = number
                break  #if it belongs here, it will exit the loop and return to the code outside the function. Same will happens whit other 'break's
            elif choice % 3 == 2:
                if grid[(2-i), 1] != 0:
                    print('You can not place here! >:(')
                    continue
                else:
                    grid[(2-i), 1] = number
                break
            elif choice % 3 == 0 :
                if grid[(2-i), 2] != 0:
                    print('You can not place here! >:(')
                    continue
                else:
                    grid[(2-i), 2] = number
                grid[(2-i), 2] = number
                break

def check_game():
    global wins_p1, wins_p2, ties, grid, end_game
    
    for i in range (3):
        if grid[i, 0] == grid[i, 1] and grid[i, 1] == grid[i, 2] and grid [i, 0] != 0:  #Checking all horizontal lines
            if grid[i, 0] == 1: #P1 wins
                print('Player 1 Won!')
                wins_p1 += 1
                grid = np.zeros((3,3), dtype=int)
                end_game = True
                return False
            
            elif grid[i, 0] == 2: #P2 wins
                print('Player 2 Won!')
                wins_p2 += 1
                grid = np.zeros((3,3), dtype=int)
                end_game = True
                return False
            
    for i in range (3):
        if grid[0, i] == grid[1, i] and grid[1, i] == grid[2, i] and grid [0, i] != 0:  #Checking all vertical lines
            if grid[0, i] == 1: #P1 wins
                print('Player 1 Won!')
                wins_p1 += 1
                grid = np.zeros((3,3), dtype=int)
                end_game = True
                return False
            
            elif grid[0, i] == 2: #P2 wins
                print('Player 2 Won!')
                wins_p2 += 1
                grid = np.zeros((3,3), dtype=int)
                end_game = True
                return False
    
    if grid[0, 0] == grid [1, 1] and grid[1, 1] == grid [2, 2] and grid [0, 0] != 0: #Checking first diagonal line
        if grid[0, 0] == 1: #P1 wins
            print('Player 1 Won!')
            wins_p1 += 1
            grid = np.zeros((3,3), dtype=int)
            end_game = True
            return False
            
        elif grid[0, 0] == 2: #P2 wins
            print('Player 2 Won!')
            wins_p2 += 1
            grid = np.zeros((3,3), dtype=int)
            end_game = True
            return False

    if grid[0, 2] == grid [1, 1] and grid[1, 1] == grid [2, 0] and grid [0, 2] != 0: #Checking second diagonal line
        if grid[0, 2] == 1: #P1 wins
            print('Player 1 Won!')
            wins_p1 += 1
            grid = np.zeros((3,3), dtype=int)
            end_game = True
            return False
            
        elif grid[0, 2] == 2: #P2 wins
            print('Player 2 Won!')
            wins_p2 += 1
            grid = np.zeros((3,3), dtype=int)
            end_game = True
            return False
    
    if 0 not in grid:     #Tie situation
        print('It is a Tie!')
        ties += 1
        grid = np.zeros((3,3), dtype=int)
        end_game = True
        return False
    
print('TIC TAC TOE\n')

print("Press 'q' anytime to quit the game\n")
print("Press 's' to check the score\n")
print('Press numbers 1-9 on your numpad to pick a position on the grid as shown:\n')
print_info()

#Starting the game

while True:
    print ('Starting a new game\n')
    print_grid()
    end_game = False

    while end_game == False:

        while True:
            print('Player 1, where would you like to apply "O"?')
            print_info()
            player_choice = input()

            if player_choice.isnumeric() and int(player_choice) > 0 and int(player_choice) < 10:
                apply_on_grid(1, int(player_choice))
                print_grid()
                check_game()
                break

            if player_choice == 's':
                print(f'P1: {wins_p1} | P2: {wins_p2} | Ties: {ties}')
                continue
            elif player_choice == 'q':
                sys.exit()

            print ('You have to type a valid input\n')
        
        if end_game == True:  #If P1 won the game on this round, The game ends here
            break

        while True:
            print('Player 2, where would you like to apply "X"?')
            print_info()
            player_choice = input()
 
            if player_choice.isnumeric() and int(player_choice) > 0 and int(player_choice) < 10:
                apply_on_grid(2, int(player_choice))
                print_grid()
                check_game()
                break

            if player_choice == 's':
                print(f'P1: {wins_p1} | P2: {wins_p2} | Ties: {ties}')
                continue
            elif player_choice == 'q':
                sys.exit()

            print ('You have to type a valid input\n')


        

