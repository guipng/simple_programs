# This is a simple guess the number game
from random import randint

secret_number = randint(1, 20)
print('I have a number between 1 and 20. Can you guess which number it is in 6 tries? \n')

# Now the player comes into action

for guessesTaken in range (1, 7):
    guess = int(input('Take a guess:\n'))
    
    if guess < secret_number:
        print(f'Your guess is too low. You have {6-guessesTaken} more guesses.')
    elif guess > secret_number:
        print(f'Your guess is too high. You have {6-guessesTaken} more guesses.')
    else:
        break #This happens when the player gets the answer

print('GAME OVER!')

if guess == secret_number:
    print(f'Good job! you guessed my number in {guessesTaken} guesses!')

else:
    print(f'You lost :(\nThe number I was thinking of was {secret_number}.')
