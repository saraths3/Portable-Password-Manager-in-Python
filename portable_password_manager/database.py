import sqlite3

conn = sqlite3.connect('database.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usertable(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20) UNIQUE,
    password VARCHAR(1000),
    admin INTEGER DEFAULT 0)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS credentials(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    platform VARCHAR(30),
    username VARCHAR(20),
    password VARCHAR(1000),
    FOREIGN KEY(user_id) REFERENCES usertable(id) ON DELETE CASCADE)
''')

conn.commit()