# this is just a small experiment on how to use libraries, sys.exit() and str manipulation

import sys

while True:
    response = input('Type exit to exit...\n')
    if response == 'exit':
        sys.exit()
    
    print(f'You tiped {response.upper()}.')