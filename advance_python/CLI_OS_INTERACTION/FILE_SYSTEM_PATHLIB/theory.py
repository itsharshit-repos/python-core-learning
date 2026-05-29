# 1) File System Thinking + pathlib

# Every projects works with folders, paths, different kind of files, etc, and they all live inside the file system,
# And python needs to answer Where am I currently running? Does this file exist? Create this folder if missing, etc.
# That is why we have pathlib. We cannot have simple strings like:
# file_path = "logs/app.log", This works but it is just a string, so we do it professionlly using pathlib:
from pathlib import Path
file_path = Path("logs")/"app.log"  # This creates a real Path object
# Means: This is not just a text, this represent a location in the file system. This is cleaner, safer and works better across 
# operating systems. 

# A) Current working directory:
from pathlib import Path
current_dir = Path.cwd()  # This tells where is python running from right now?
print(current_dir)

# B) Creating a path:
from  pathlib import Path
log_file = Path("logs")/"app.log"  # Why '/'? Because pathlib overloads / to join paths cleanly.
print(log_file)

# C) Check if file/folder exists
from pathlib import Path
path = Path("config.json")
if path.exists():
    print("config found")
else:
    print("config missing")

# D) Create folder
from pathlib import Path
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)  # Means create folder named 'logs' and if it already exist, don't crash
# This part of exist_ok=True is important, without it python throw error if folder already exist
Path("storage/logs/errors").mkdir(parents=True, exist_ok=True) # parents=True create parent folder also if needed.
# If storage/ does not exist, python create it too.

# E) Write text file
from pathlib import Path
log_file = Path("logs")/"app/log"
log_file.write_text("AI system started") # But remember this write function will overwrite the file data, and write new

# F) Read text file
from pathlib import Path
log_file = Path("logs")/"app/log"
content = log_file.read_text()
print(content)

# G) Find files in folder 
from pathlib import Path
data_dir = Path("data")
for file in data_dir.iterdir():
    print(file)
# TO FIND ALL JSON FILES
from pathlib import Path
for file in Path("models").glob("*.json"):
    print(file)

# REAL LIFE EXAMPLE CODE -

# Imagine your AI system needs this structure:
# ai_system/
# ├── main.py
# ├── config/
# │   └── settings.json
# ├── logs/
# │   └── app.log
# └── workspaces/
from pathlib import Path

BASE_DIR = Path.cwd()
CONFIG_DIR = BASE_DIR/"config"
LOGS_DIR = BASE_DIR/"logs"
WORKSPACES_DIR = BASE_DIR/"workspaces"

CONFIG_FILE = CONFIG_DIR/"settings.json"
LOGS_FILE = LOGS_DIR/"app.log"

def setup_project_folder() -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    WORKSPACES_DIR.mkdir(parents=True, exist_ok=True)
def create_default_config() -> None:
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text('{"app_name": "AI System", "version": "1.0"}')
def main() -> None:
    setup_project_folder()
    create_default_config()
    LOGS_FILE.write_text("AI System initialized")
    print("Project setup completed")

if __name__ == "__main__":
    main()

# IMPORTANT ENGINEERING RULE:
# 1) Use 'PATHLIB' - for files/folders path
# 2) Use 'OS' - for operating system environment, low level system interactions, and environment variables
# 3) Use 'SUBPROCESS' - when python needs to run external commands like git status, pytest, docker build, python script.py

