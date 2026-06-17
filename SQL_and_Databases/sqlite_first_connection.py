import sqlite3

connection = sqlite3.connect('learning.db')
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
"""
)

cursor.execute(
    """
INSERT INTO users (name, email)
VALUES (?,?)
""",
("Harshit Kumar", "Harshit@example.com"),
)

connection.commit()

cursor.execute(
    """
SELECT id, name, email
FROM users
ORDER BY id
"""
)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()