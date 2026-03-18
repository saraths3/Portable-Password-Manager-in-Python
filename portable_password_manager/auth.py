import hashlib, sqlite3
from database import cursor, conn
from menu import usermenu, adminmenu
import questionary, clearscreen, session


def u_signup():
    clearscreen.clearscreen()
    uname = questionary.text("Enter Username: ", qmark='').ask()
    if not uname or len(uname) < 5:
        print("Username must be at least 5 characters.")
        return
    cursor.execute("SELECT 1 FROM usertable WHERE username = ?", (uname,))
    if cursor.fetchone():
        print("Username already exists.")
        return
    upass = questionary.password("Enter Password: ", qmark='').ask()
    if not upass or len(upass) < 8 or upass.isalnum():
        print("Password must be 8+ chars and include a symbol.")
        return
    hashed_pass = hashlib.sha256(upass.encode()).hexdigest()
    try:
        cursor.execute(
            "INSERT INTO usertable(username, password) VALUES(?, ?)",
            (uname, hashed_pass)
        )
        conn.commit()
        print("Signup successful.")
    except sqlite3.IntegrityError:
        print("Username already exists.")


def u_signin():
    clearscreen.clearscreen()
    uname = questionary.text("Enter Username: ", qmark='').ask()
    if not uname or len(uname) < 5:
        print("Invalid username.")
        return
    upass = questionary.password("Enter Password: ", qmark='').ask()
    if not upass:
        print("Invalid password.")
        return
    hashed_pass = hashlib.sha256(upass.encode()).hexdigest()
    cursor.execute(
        "SELECT * FROM usertable WHERE username = ? AND password = ?",
        (uname, hashed_pass)
    )
    identity = cursor.fetchone()
    if not identity:
        print("Invalid credentials.")
        return
    session.current_user_id = identity[0]
    if identity[3] == 1: adminmenu()
    else: usermenu()

    session.current_user_id = None
