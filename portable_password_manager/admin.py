import hashlib, sqlite3
from database import cursor, conn
from tabulate import tabulate
import questionary, clearscreen

class AdminClass:
    def add_admin(self):
        clearscreen.clearscreen()
        uname = questionary.text("Enter Admin Username: ").ask()
        clearscreen.clearscreen()

        if len(uname) < 5:
            print('Username should atleast \nhave 5 characters ')
            return
        upass = questionary.password("Enter Admin Password: ").ask()
        clearscreen.clearscreen()

        if len(upass) < 8 or upass.isalnum():
            print("Password needs 8+ characters and at least one symbol")
        clearscreen.clearscreen()
        hashed_pass = hashlib.sha256(upass.encode()).hexdigest()

        try:
            cursor.execute(
                '''INSERT INTO usertable(username, password, admin)
                VALUES(?,?, 1)''',
                (uname, hashed_pass))
            conn.commit()
            print('Admin signup successful.')
        except sqlite3.IntegrityError:
            print('Username already exists.')

    def view_users(self):
        clearscreen.clearscreen()
        cursor.execute("SELECT id, username, admin FROM usertable")
        data = cursor.fetchall()

        if data:
            print(tabulate(data, headers=["ID", "Username", "Admin Status"], tablefmt="grid"))
        else:
            print("No users found.")

    def delete_user(self):
        clearscreen.clearscreen()
        uname = questionary.text("Enter username to delete: ").ask()
        clearscreen.clearscreen()
        cursor.execute(
            "DELETE FROM usertable WHERE username = ?",
            (uname,)
        )
        conn.commit()
        print("Admin deleted.")

admin = AdminClass()