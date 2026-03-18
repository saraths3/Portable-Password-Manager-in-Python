import time, clearscreen

current_user_id = None

from pyfiglet import figlet_format



def intro_screen():
    clearscreen.clearscreen()
    inn = figlet_format("WELCOME")

    for  i in inn:
        print(i,end="", flush = True)
        time.sleep(0.01) 

