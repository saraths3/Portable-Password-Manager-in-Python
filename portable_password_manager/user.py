from database import cursor, conn
from crypto import cipher_suite
from tabulate import tabulate
import session, questionary, clearscreen, lline

class UserClass:
    def insert_c(self):
        clearscreen.clearscreen()
        plat = questionary.text("Platform Name: ", qmark ='').ask()
        u_name = questionary.text("Enter Username: ", qmark='').ask()
        u_pass = questionary.password("Enter Password: ", qmark='').ask()
        clearscreen.clearscreen()
        cipher_pass = cipher_suite.encrypt(u_pass.encode())
        cursor.execute(
            '''INSERT INTO credentials(user_id, platform, username, password)
            VALUES(?, ?, ?, ?)''',
            (session.current_user_id, plat, u_name, cipher_pass))
        conn.commit()
        lline.i_line()

    def update_c(self):
        clearscreen.clearscreen()
        plat = questionary.text("Enter Platform: ", qmark='').ask()
        clearscreen.clearscreen()
        cursor.execute(
            '''SELECT * FROM credentials WHERE platform = ? AND user_id = ?''',
            (plat, session.current_user_id))
        data = cursor.fetchone()

        if data:
            u_name = questionary.text("Enter Username: ", qmark='').ask()
            u_pass = questionary.text("Enter Password: ", qmark='').ask()
            clearscreen.clearscreen()
            cipher_pass = cipher_suite.encrypt(u_pass.encode())
            cursor.execute(
                '''UPDATE credentials SET username = ?, password = ?
                WHERE platform = ? AND user_id = ?''',
                (u_name, cipher_pass, plat, session.current_user_id))
            conn.commit()
            lline.u_line()
        else:
            print('Credential not found.')

    def view_c(self):
        clearscreen.clearscreen()
        cursor.execute(
            '''SELECT id, platform, username, password FROM credentials WHERE user_id = ?''',
            (session.current_user_id,))
        data = cursor.fetchall()

        print(len(data), 'Credentials Found')
        if data:
            decrypted_data = []
            for row in data:
                plain_pass = cipher_suite.decrypt(row[3]).decode()
                decrypted_data.append([row[1], row[2], plain_pass])

            headers = ["Platform", "Username", "Password"]
            print(tabulate(decrypted_data, headers=headers, tablefmt="grid"))
        else:
            print("Table is empty")

    def delete_c(self):
        clearscreen.clearscreen()
        confirm = questionary.text("Confirm (y): ", qmark='').ask()
        if confirm.lower() == 'y':
            plat = questionary.text("Enter Platform: ", qmark='').ask()
            clearscreen.clearscreen()
            cursor.execute(
                '''DELETE FROM credentials WHERE platform = ? AND user_id = ?''',
                (plat, session.current_user_id))
            conn.commit()
            lline.d_line()

user = UserClass()