# Context managers and guarenteed cleanup

# You already know manual cleanup:
# cursor.close()
# connection.close()
# The problem is that an unexpected exception can prevent these lines from running unless cleanup is protected.
# Context managers help guarantee cleanup. 

# Two separate responsibilities
# With SQLite, these are different:
# Transaction management -> commit or rollback
# Resource management    -> close the connection

# This distinction matters because:
# with sqlite3.connect("example.db") as connection:
#     ...
# automatically commits on success and rolls back on failure, but it does not necessarily close the connection when the block ends.
# So we will use:  from contextlib import closing

# reliable structure:
# import sqlite3
# from contextlib import closing
# with closing(sqlite3.connect("example.db")) as connection:
#     connection.row_factory = sqlite3.Row
#     with connection:
#         connection.execute(
#             """
#             INSERT INTO <table_name> (<column 1>,<column 2>)
#             VALUES (?,?)
#             """,
#             ("<value 1>", "<value 2>")
#         )

# The structure is:
# Open connection
#     ↓
# Start transaction block
#     ↓
# Commit or rollback automatically
#     ↓
# Close connection automatically

# You often do not need a separate cursor variable
# The connection itself can execute SQL:
# connection.execute(
#     "SELECT id, name FROM projects"
# )

# It returns a cursor:
# cursor = connection.execute(
#     "SELECT id, name FROM projects"
# )
# rows = cursor.fetchall()

# Both styles are valid:
# cursor = connection.cursor()
# cursor.execute(...)

# or:

# cursor = connection.execute(...)
# For short database functions, connection.execute() is often cleaner.

# Automatic rollback example
# try:
#     with closing(sqlite3.connect("example.db")) as connection:
#         with connection:
#             connection.execute(
#                 """
#                 INSERT INTO users (name, email)
#                 VALUES (?, ?)
#                 """,
#                 ("Harshit", "harshit@example.com"),
#             )

#             connection.execute(
#                 """
#                 INSERT INTO users (name, email)
#                 VALUES (?, ?)
#                 """,
#                 ("Duplicate", "harshit@example.com"),
#             )

# except sqlite3.IntegrityError as error:
#     print(f"Transaction failed: {error}")

# Important rule:
# Catch database errors outside the transaction block when you want automatic rollback.
# Correct:
# try:
#     with connection:
#         # Database writes that may fail.
# except sqlite3.IntegrityError:
#     # The transaction has already rolled back.

# Be careful with this:
# with connection:
#     try:
#         # Failing database operation.
#     except sqlite3.IntegrityError:
#         print("Ignored")

# If you catch and suppress the error inside the transaction block, the context manager may think the block finished successfully 
# and attempt to commit other changes.

# CODING TASK:
import sqlite3
from contextlib import closing

# auto closing connection and transaction using context managers
with closing(sqlite3.connect("module1_lesson6.db")) as connection:
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    with connection:
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            credit_balance INTEGER NOT NULL CHECK (credit_balance >= 0)
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS usage_logs (
            id INTEGER PRIMARY KEY,
            project_id INTEGER NOT NULL,
            credits_charged INTEGER NOT NULL CHECK (credits_charged >= 0),
            FOREIGN KEY (project_id) REFERENCES projects(id)
        )
        """
        )

        cursor.execute(
        "INSERT INTO projects (name, credit_balance) VALUES (?,?)",
        ("Model API", 500),
        )
        project_id = cursor.lastrowid
        print(f"Created project ID: {project_id}")

    # the safe rollback phase
    try:
        with connection:
            cursor.execute(
            "UPDATE projects SET credit_balance = credit_balance - 100 WHERE id = ?",
            (project_id,)
            )

            cursor.execute(
                "INSERT INTO usage_logs (project_id, credits_charged) VALUES (?,?)",
                (project_id, -100),
            )
    except sqlite3.IntegrityError as error:
        print(f"Transaction failed: {error}")

    cursor.execute(
        """
    SELECT credit_balance FROM projects WHERE id = ?
    """,
    (project_id,)
    )

    balance = cursor.fetchone()[0]
    print(f"Final credit balance: {balance}")