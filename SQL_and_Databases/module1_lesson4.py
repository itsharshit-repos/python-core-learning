# "rowcount" and checking whether a write actually changed anything
# "rowcount" answers: How many rows did my latest UPDATE or DELETE affects!

# Basic example -
# cursor.execute(
#     """
#     UPDATE projects
#     SET credit_balance = credit_balance - ?
#     WHERE id = ?
#     """,
#     (100, 1),
# )
# print(cursor.rowcount)
# Possible result: 1 (Meaning one project was updated.)

# If project 999 does not exist:
# cursor.execute(
#     """
#     UPDATE projects
#     SET credit_balance = credit_balance - ?
#     WHERE id = ?
#     """,
#     (100, 999),
# )
# print(cursor.rowcount)
# Result: 0 (No row matched the condition.)

# Without checking rowcount, your program may assume the deduction succeeded when it did not.

# rowcount with DELETE
# cursor.execute(
#     "DELETE FROM projects WHERE id = ?",
#     (project_id,),
# )
# deleted_rows = cursor.rowcount
# If deleted_rows == 0, nothing was deleted.

# Important limitation: For SELECT, do not use rowcount to determine how many results exist. In SQLite, it may remain -1.

# CODING TASK:
import sqlite3

# establishing connection
connection = sqlite3.connect("module1_lesson4.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

# creating table if not exist
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    credit_balance INTEGER NOT NULL DEFAULT 0
)
"""
)

# inserting data into the table
cursor.execute(
    """
INSERT INTO projects (name, credit_balance) VALUES (?,?)
""",
("Model Serving Platform", 500),
)

project_id = cursor.lastrowid
print(f"Created project ID: {project_id}")

# updating the data into the table
cursor.execute(
    """
UPDATE projects 
SET credit_balance = credit_balance - ?
WHERE id = ? AND credit_balance >= ?
""",
(150,project_id,150),
)
# counting successful rows
print(f"Successful deduction affected rows: {cursor.rowcount}")

# updating data into the table
cursor.execute(
    """
UPDATE projects 
SET credit_balance = credit_balance - ?
WHERE id = ? AND credit_balance >= ?
""",
(500,project_id,500),
)

print(f"Failed deduction affected: {cursor.rowcount}")

# commiting connection
connection.commit()

# selecting data from table
cursor.execute(
    """
SELECT id, name, credit_balance FROM projects
WHERE id = ?
""",
(project_id,),
)

# fetching data
project = cursor.fetchone()
print(f"Final project: {dict(project)}")

# closing connection
cursor.close()
connection.close()