# execute(), executemany(), lastrowid, and fetch methods

# 1) execute() : runs one SQL statement once. One tuple of values produces one inserted row. Example -
# cursor.execute(
#     """
# INSERT INTO projects (name, credit_balance) VALUES (?,?),
# ("Project A", 200),
# """
# )

#--------------------------------------------------------------------------------------------------------------------------------

# executemany() : When inserting several rows, do not repeatedly copy the same execute() call
# projects = [
#     ("Project B", 300),
#     ("Project C", 400),
#     ("Project D", 500),
# ]
# cursor.executemany(
#     """
# INSERT INTO projects (name, credit_balance) VALUES (?,?),
# projects,
# """
# )

# Conceptually, SQLite executes the same statement once for every tuple:
# ("Project B", 300)
# ("Project C", 400)
# ("Project D", 500)
# This is cleaner and usually more efficient than manually writing several inserts.

#-------------------------------------------------------------------------------------------------------------------------------

# lastrowid() : gives the ID generated for that inserted row. After inserting one row using execute() -
# cursor.execute(
#     "INSERT INTO projects (name, credit_balance) VALUES (?, ?)",
#     ("Project A", 200),
# )

# new_project_id = cursor.lastrowid
# print(new_project_id)

#------------------------------------------------------------------------------------------------------------------------------

# fetchone() : After a SELECT, it returns the next row. If no row remains, it returns None. 
# cursor.execute(
#     "SELECT id, name FROM projects WHERE id = ?",
#     (project_id,),
# )

# project = cursor.fetchone()

# if project is None:
#     print("Project not found")
# else:
#     print(project)

#-------------------------------------------------------------------------------------------------------------------------------

# fetchmany(size): This returns upto 2 next rows.
# rows = cursor.fetchmany(2)
# If only one row remains, it returns one row. 

#-------------------------------------------------------------------------------------------------------------------------------

# CODING TASK:
import sqlite3

connection = sqlite3.connect("module1_lesson2.db")
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    credit_balance INTEGER NOT NULL DEFAULT 0
)
"""
)

cursor.execute(
    """
INSERT INTO projects (name, credit_balance) VALUES (?,?)
""",
("Single Project", 100),
)

new_project_id = cursor.lastrowid
print(new_project_id)

projects = [
    ("Analytics Project", 200),
    ("Memory Project", 300),
    ("Agent Project", 400),
]
cursor.executemany(
    """
INSERT INTO projects (name, credit_balance) VALUES (?,?)
""",
(projects),
)

connection.commit()

cursor.execute(
    """
SELECT id, name, credit_balance 
FROM projects
ORDER BY id
"""
)

first_project = cursor.fetchone()
next_two_projects = cursor.fetchmany(2)
remaining_projects = cursor.fetchall()

print(f"First: {first_project}\nNext two: {next_two_projects}\nRemaining: {remaining_projects}")

cursor.close()
connection.close()