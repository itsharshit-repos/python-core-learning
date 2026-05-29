# CODING TASK:
# Create a file: config_loader.py
# Write code that: imports os, imports dataclass
# creates:
# @dataclass
# class AppConfig:
#     app_name: str
#     environment: str
#     port: int
#     debug: bool
# creates function:
# def load_config() -> AppConfig:
# It should read: APP_NAME, APP_ENV, PORT, DEBUG using os.getenv().
# Defaults:
# APP_NAME = AI Workspace System
# APP_ENV = development
# PORT = 8000
# DEBUG = false
# In main(), print the config.
# Use:
# if __name__ == "__main__":
#     main()

import os 
from dataclasses import dataclass

@dataclass
class AppConfig:
    app_name: str
    environment: str
    port: int
    debug: bool

def load_config() -> AppConfig:
    return AppConfig(
        app_name=os.getenv("APP_NAME", "AI Workspace System"),
        environment=os.getenv("APP_ENV", "development"),
        port=int(os.getenv("PORT", "8000")),
        debug=os.getenv("DEBUG", "false").lower() == "true"
    )

def main() -> None:
    config = load_config()
    print(config)

if __name__ == "__main__":
    main()

# Suppose if in line "port=int(os.getenv("PORT", "8000"))", someone wrote "abc" in PORT, then it will crash, so we can refine it
# by implementng this, so that in production, system can handle it with much safety.

# def get_int_env(name: str, default: int) -> int:
#     value = os.getenv(name)
#     if value is None:
#         return default
#     try:
#         return int(value)
#     except ValueError:
#         raise RuntimeError(f"{name} must be an integer") 

# Then after writing this, you can write safely,  'port=get_int_env("PORT",8000)'

# UPGRADED VERSION:---------------------------------------------------------------------------

# import os
# from dataclasses import dataclass

# @dataclass
# class AppConfig:
#     app_name: str
#     environment: str
#     port: int
#     debug: bool

# def get_int_env(name: str, default: int) -> int:
#     value = os.getenv(name)

#     if value is None:
#         return default

#     try:
#         return int(value)
#     except ValueError:
#         raise RuntimeError(f"{name} must be an integer")

# def get_bool_env(name: str, default: bool) -> bool:
#     value = os.getenv(name)

#     if value is None:
#         return default

#     return value.lower() == "true"

# def load_config() -> AppConfig:
#     return AppConfig(
#         app_name=os.getenv("APP_NAME", "AI Workspace System"),
#         environment=os.getenv("APP_ENV", "development"),
#         port=get_int_env("PORT", 8000),
#         debug=get_bool_env("DEBUG", False),
#     )

# def main() -> None:
#     config = load_config()
#     print(config)

# if __name__ == "__main__":
#     main()