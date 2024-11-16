import sqlite3

conn = sqlite3.connect('obituary_platform.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS obituaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date_of_birth DATE,
    date_of_death DATE,
    content TEXT,
    author TEXT,
    submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    slug TEXT UNIQUE
)''')

conn.commit()
conn.close()

print("Database and table created successfully.")
