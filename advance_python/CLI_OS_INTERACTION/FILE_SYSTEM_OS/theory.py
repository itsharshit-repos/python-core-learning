# OS is mainly for:
# operating system interaction
# environment variables
# runtime environment
# some file operations

# For AI/Backend engineering, the most important OS concept is: ENVIRONMENT VARIABLES
# Why they exist? Bad code:
# API_KEY = "sk-abc123"
# DATABASE_URL = "postgres://user:pass@localhost/db"
# SECRET_KEY = "mysecret"
# We must NOT hard code our API keys into the main code and push it to GitHub, thats BAD, that is why we use: os.getenv()
import os
api_key = os.getenv("API_KEY")  # make file named 'anyname.env' in the folder. REMEMBER to add it in 'gitignore' so that it doesn't
# get pushed to github along with other code.
# This line, os.getenv("API_KEY") means “Get the API key from the operating system environment, not from the source code.”

#------------------------------------------------------------------------------------------------------------------------------

# Default Value - You can provide fallback
import os
app_env = os.getenv("APP_ENV", "development") # Means “Get APP_ENV. If it does not exist, use development.”
print(app_env)

#------------------------------------------------------------------------------------------------------------------------------

# Environment variable are strings
# If you set PORT=8000, Python receives "8000" NOT 8000, So we often convert
import os
port = int(os.getenv("PORT", "8000"))
print(port)
# Same with boolean
debug = os.getenv("DEBUG", "false").lower() == "true"  # Explanation below -
# Phase 1: os.getenv("DEBUG", "false") -
# The system attempts to look for a configuration variable named "DEBUG" inside your operating system's environment.
# If it finds it: It reads whatever text is stored inside it (for example, "TRUE" or "False").
# If it does NOT find it: It safely defaults to the string "false" instead of crashing your program.
# Phase 2: .lower() -
# Environment variables are often typed erratically by humans or cloud servers (like "True", "TRUE", or "true"). Appending 
# .lower() converts whatever string was fetched in Phase 1 into completely lowercase letters to guarantee consistency.
# Phase 3: == "true" -
# This is the evaluation check. It compares the lowercase string from Phase 2 against the literal string "true".
# If they match, the statement becomes True (a boolean).
# If they don't match, it becomes False

#------------------------------------------------------------------------------------------------------------------------------

# os.environ()
# There are 2 common ways: Read using os.getenv(), This is safer because it returns None if missing, BUT
# Use os.environ["API_KEY"] only when the variable is absolutely required and you want the app to crash if missing.

#------------------------------------------------------------------------------------------------------------------------------

# Required secret pattern - For something like API key:
import os
def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value
api_key = get_required_env("API_KEY")
# This is professional because instead of failing randomly later, you app clearly says:
# Missing required environment variable: API_KEY
