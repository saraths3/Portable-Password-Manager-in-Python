# Portable Password Manager (CLI)
![Workflow](https://raw.githubusercontent.com/saraths3/Portable-Password-Manager-in-Python/main/banner.png)
## Requirements

Install dependencies:

```bash
pip install cryptography questionary tabulate pyfiglet
```

---

## Project Structure

*  → Entry point
*  → Authentication (signup/login)
*  → Admin features
*  → User credential management
*  → Menus
*  → Database setup (SQLite)
*  → Encryption (Fernet)
*  → Session handling
*  → Clear screen utility
*  → UI lines/messages

---

## How to Run

```bash
python main.py
```

---

## First Run Behavior

* `database.db` is created automatically 
* `secret.key` is generated automatically 

---

## Usage Flow

1. Run program
2. Choose:

   * SignUp
   * SignIn
3. After login:

   * User → Credential management menu
   * Admin → User management menu

---

## Modules Used

* `sqlite3` → Database
* `hashlib` → Password hashing
* `cryptography` → Password encryption
* `questionary` → CLI prompts
* `tabulate` → Table display
* `pyfiglet` → ASCII banner
* `os`, `time` → System utilities

---

## Notes

- Admin accounts must be set manually:
  - Create a user normally
  - Open `database.db`
  - In the `usertable`, set `admin = 1` for that user

- Session is handled using a global variable: `session.current_user_id`

- Password handling:
  - Login passwords → Hashed using SHA256
  - Stored credentials → Encrypted using Fernet

---

