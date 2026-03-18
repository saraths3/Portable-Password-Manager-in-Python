import hashlib, sqlite3
from database import cursor, conn
from menu import usermenu, adminmenu
import questionary, clearscreen, session

def u_signup():
    clearscreen.clearscreen()
    uname = questionary.text("Enter Username: ", qmark ='').ask()
    if len(uname) < 5:
        clearscreen.clearscreen()
        print('Username should atleast \nhave 5 characters ')
        return
    cursor.execute("SELECT * FROM usertable WHERE username = ?", (uname,))
    if cursor.fetchone():
        clearscreen.clearscreen()
        print("Username already exists.")
        return
    upass = questionary.password("Enter Password: ", qmark ='').ask()
    if len(upass) < 8 or upass.isalnum():
        clearscreen.clearscreen()
        print("Password needs 8 or more characters\nand at least one symbol")
        return
    hashed_pass = hashlib.sha256(upass.encode()).hexdigest()
    clearscreen.clearscreen()
    try:
        cursor.execute(
            '''INSERT INTO usertable(username, password)
            VALUES(?,?)''',
            (uname, hashed_pass))
        conn.commit()
        print('Signup successful.')
    except sqlite3.IntegrityError:
        clearscreen.clearscreen()
        print('Username already exists.')

def u_signin():
    clearscreen.clearscreen()
    uname = questionary.text("Enter Username: ", qmark ='').ask()
    if len(uname) < 5:
        clearscreen.clearscreen()
        print('Username should atleast \nhave 5 characters')
        return
    upass = questionary.password("Enter Password: ", qmark ='').ask()
    if len(upass) < 8 or upass.isalnum():
        clearscreen.clearscreen()
        print("Password needs 8 or more characters\nand at least one symbol")
        return
    hashed_pass = hashlib.sha256(upass.encode()).hexdigest()

    cursor.execute(
        '''SELECT * FROM usertable
        WHERE username = ? AND password = ?''',
        (uname, hashed_pass))

    identity = cursor.fetchone()

    if identity:
        session.current_user_id = identity[0]

        if identity[3] == 1: adminmenu()
        else: usermenu()
        session.current_user_id = None
    else:
        clearscreen.clearscreen()
        print('Invalid credentials. Try Again.')
