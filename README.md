# Portable Password Manager (CLI)

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

* Session handled via global variable: `session.current_user_id` 
* Passwords:

  * Login → Hashed (SHA256)
  * Stored credentials → Encrypted (Fernet)

---

