from database import conn
from auth import u_signup, u_signin
import clearscreen, lline, questionary, session

def mainmenu():
    
    clearscreen.clearscreen()
    session.intro_screen()

    while True:
        lline.head()
        choice = questionary.select(f'Select the Option',
            choices=['SignUp', 'SignIn', f'Exit'], qmark ='', pointer ='➤').ask()
        
        if choice == 'SignUp': u_signup()
        elif choice == 'SignIn': u_signin()
        elif choice == 'Exit': conn.close();clearscreen.clearscreen(); break
    

mainmenu()
