import questionary, clearscreen
from user import user
from admin import admin

def usermenu():
    clearscreen.clearscreen()
    
    while True:
        choice = questionary.select("\nUser Menu",choices=["Add Credential", "Update Credential",
        "View All", "Delete Credential", "Logout"], qmark ='', pointer ='➤').ask()

        if choice == "Add Credential": user.insert_c()
        elif choice == "Update Credential": user.update_c()
        elif choice == "View All": user.view_c()
        elif choice == "Delete Credential": user.delete_c()
        elif choice == "Logout": clearscreen.clearscreen(); break


def adminmenu():
    clearscreen.clearscreen()
    while True:
        choice = questionary.select("\nAdmin Menu", choices=["View Users", "Add Admin", "Delete User", "Logout"], qmark ='', pointer ='➤').ask()

        if choice == "View Users": admin.view_users()
        elif choice == "Add Admin": admin.add_admin()
        elif choice == "Delete User": admin.delete_user()
        elif choice == "Logout":clearscreen.clearscreen(); break