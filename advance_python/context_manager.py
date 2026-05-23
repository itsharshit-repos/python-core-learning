# We currently know 'with'
# with open('file.txt') as f:
# WHAT 'with' ACTUALLY DOES:
# with open("data.txt") as f:
#    data = f.read()
# internally behaves SIMILARLY to:
# f = open("data.txt")
# try:
#     data = f.read()
# finally:
#     f.close()
# THAT is the key idea.
# Context Managers Guarantee Cleanup
# Even if:
# error happens
# crash happens
# exception occurs
# cleanup STILL runs.
# Main purpose: It acts as a safety net that guarantees a system resource (like a database connection, a network socket, or a 
# file lock) is always cleanly set up and completely shut down, even if your code crashes in the middle of a task.

# HOW PYTHON DOES THIS
# Using two magic methods:
# __enter__()
# __exit__()

# SIMPLE CUSTOM CONTEXT MANAGER
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database...")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Closing database connection...")
with DatabaseConnection() as db:
    print("Running queries...")


# CODING TASK: 
# Create: class AISession
# Requirements: When entering: Starting AI session...
# Inside block: user prints something
# When exiting: Closing AI session...
# Usage:
# with AISession() as ai:
#     print("Generating AI response...")
# BONUS: Inside __exit__, print: exc_type, if an error occurs.
class AISession:
    def __enter__(self):
        print("Starting AI session...")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Closing AI session...")
        if exc_type:
            print(f"Error occured: {exc_type}")
with AISession() as ais:
    print("Generating AI response...")
# NOW if anyhow error occurs also still it will close the connection! This is the main superpower of this, and help large system.

# MINI CHALLENGE 
import time
class AISession:
    def __init__(self):
        self.start_time = None
    def __enter__(self):
        self.start_time = time.time()
        print("Starting AI session...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing AI connection...")
        total_duration = time.time() - self.start_time
        print(f"Session duration: {total_duration:.2f} seconds")
        if exc_type:
            print(f"AI session crashed safely: {exc_val}")
            return True
with AISession() as session:
    time.sleep(2.45)
print("Session finished normally.")
# Testing the crash handling
with AISession() as session:
    time.sleep(1.0)
    result = 10/0
print("Status: System recovered and continued moving forward flawlessly!")

