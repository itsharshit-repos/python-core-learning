# sqlite3.Row -

# Tuple rows vs dictionary like rows:
# Currently SQLite gives you rows as tuples: (1, "Single Project", 100). To access the project name: project_name = row[1]
# This works, but it is fragile. 
# Suppose your query changes from: SELECT id, name, credit_balance, to: SELECT name, id, credit_balance.
# Now: row[1] means id, not name. In larger system, such codes becomes difficult to read. That is why we have sqlite.Row

# SQLite can return dictionary like row objects. Set this immediately after creating the connection.
# connection = sqlite.connect(__database_name__)
# connection.row_factory = sqlite.Row

# Then create the cursor
# cursor = connection.cursor()

# Now after executing, you can access values by column name
# row = cursor.fetchone()
# print(row["id"])
# print(row["name"])
# print(row["credit_balance"])

# This is clearer than:
# print(row[0])
# print(row[1])
# print(row[2])

# complete example -

# connection = sqlite3.connect("projects.db")
# connection.row_factory = sqlite3.Row
# cursor = connection.cursor()

# cursor.execute("""
# SELECT id, name, credit_balance
# FROM projects
# ORDER BY id
# """)

# rows = cursor.fetchall()

# for row in rows:
#     print(row["id"])
#     print(row["name"])
#     print(row["credit_balance"])

#     project_dictionary = dict(row)
#     print(project_dictionary)

# cursor.close()
# connection.close()

# Why this connects to professional backend work
# Later, SQLAlchemy will return model objects:
# project.id
# project.name
# project.credit_balance
# But raw drivers often return row-like results.

# CODING TASK
import sqlite3

# establishing connection
connection = sqlite3.connect("module1_lesson3.db")
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
projects = [
    ("Vision System", 600),
    ("RAG Platform", 800),
    ("Agent Runtime", 1000),
]
cursor.executemany(
    """
INSERT INTO projects (name, credit_balance) VALUES (?,?)
""",
projects,
)
# commiting insert
connection.commit()

# selecting data from table
cursor.execute(
    """
SELECT id, name, credit_balance FROM projects
ORDER BY id
"""
)

rows = cursor.fetchall()
# fetching data
for row in rows:
    print(f"Project ID: {row['id']}\nName: {row['name']}\nCredits: {row['credit_balance']}\nAs dictionary: {dict(row)}")

# closing connection
cursor.close()
connection.close()