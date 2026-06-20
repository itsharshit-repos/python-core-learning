# commit(), rollback() and Exception Handling :
# Until now, your code assumed every database operation succeeds

# Real systems fail:
# - duplicate email
# - invalid foreign key
# - negative value rejected by a constraint
# - database locked
# - wrong SQL
# - application crashes between two operations
# We need to ensure a partial operation is not saved.

# The problem: Suppose these two actions belong together:
# 1. Deduct credits
# 2. Insert usage log
# If deduction succeeds but log insertion fails, we do not want to keep the deduction.
# That is why we use: connection.commit() when everything succeeds, 
# and: connection.rollback() when something fails.

# Basic structure:-
# try:
#     # Perform related database writes.
#     connection.commit()
# except sqlite3.Error as error:
#     connection.rollback()
#     print(f"Database error: {error}")

# Important point: rollback() only cancels changes made after the previous commit.

# Exception types:
# For now, know these two: 
# 1) sqlite3.Error 
# Base class for SQLite database errors.
# 2) sqlite3.IntegrityError

# CODING TASK
import sqlite3

connection = sqlite3.connect("module1_lesson5.db")
cursor = connection.cursor()

# create table if not exist
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
"""
)

# handling error cases using try/except
try:
    cursor.execute(
        """
    INSERT INTO users (name, email) VALUES (?,?)
    """,
    ("Harshit Kumar", "harshit@example.com"),
    )

    cursor.execute(
        """
    INSERT INTO users (name, email) VALUES (?,?)
    """,
    ("Duplicate User", "harshit@example.com"),
    )

    connection.commit()

except sqlite3.IntegrityError as error:
    connection.rollback()
    print(f"Transaction failed: {error}")

finally:
    cursor.execute(
        """
    SELECT id, name, email FROM users
    ORDER BY id
    """
    )

    users = cursor.fetchall()
    print(f"Users stored after transaction: {users}")

    cursor.close()
    connection.close()