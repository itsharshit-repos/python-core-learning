import sqlite3

# Establishing connection
connection = sqlite3.connect("module1_lesson1.db")
cursor = connection.cursor()

# create table if not exist
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    credit_balance INTEGER NOT NULL DEFAULT 0
)
"""
)
# inserting value into the table
cursor.execute(
    """
INSERT INTO projects (name, credit_balance)
VALUES (?,?)
""",
("Friday_AI_Backend", 500),
)
# commiting the value insertion
connection.commit()

# selecting the columns we want
cursor.execute(
    """
SELECT id, name, credit_balance
FROM projects
ORDER BY id
"""
)
# fetching the data
rows = cursor.fetchall()
for row in rows:
    print(row)
    
# closing connection
cursor.close()
connection.close()