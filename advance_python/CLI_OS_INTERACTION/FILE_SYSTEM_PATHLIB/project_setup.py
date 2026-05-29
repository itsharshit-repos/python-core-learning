# CODING TASK:
# Create a file called: project_setup.py
# Write code that: Imports Path
# Creates these folders: logs, data, models, config
# Creates a file: config/settings.txt
# Writes this inside it: app_name=AI Workspace System, version=1.0
# Reads the file and prints its content
# Uses: def main() -> None:   AND 
# if __name__ == "__main__":
#     main()
# This task combines: pathlib, typing, main guard, project structure thinking.

from pathlib import Path  # log, data, model, config

BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR/"logs"
DATA_DIR = BASE_DIR/"data"
MODELS_DIR = BASE_DIR/"models"
CONFIG_DIR = BASE_DIR/"config"

CONFIG_FILE = CONFIG_DIR/"settings.txt"

def initial_folder_setup() -> None:
    # LOGS_DIR.mkdir(parents=True, exist_ok=True)
    # DATA_DIR.mkdir(parents=True, exist_ok=True)
    # MODELS_DIR.mkdir(parents=True, exist_ok=True)
    # CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    # or simply
    folders = [LOGS_DIR, DATA_DIR, MODELS_DIR, CONFIG_DIR]
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

def create_default_config() -> None:
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(
            "app_name = AI Workspace System\n"
            "version = 1.0\n",
            encoding="utf-8"
        )

def main() -> None:
    initial_folder_setup()
    create_default_config()
    content = CONFIG_FILE.read_text(encoding="utf-8")
    print(content)

if __name__ == "__main__":
    main()
