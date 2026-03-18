import os

def clearscreen():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

clearscreen()