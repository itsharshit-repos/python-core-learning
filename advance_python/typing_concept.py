# Typing means we will follow perticular structure, for example without typing method,
# def add(a,b):
#     return a + b
# Now here, a and b can be anything either int, it will return sum or string 'a'+'b'='ab'
# But with typing method, we can define what data type should go as input and come out as output
def generate(prompt: str) -> str:  # How simple, means "Give me a string prompt, and I promise to return a string."
    return f"AI response for: {prompt}"

# Example 1 as prefessional version:
def add(a: int, b: int) -> int:
    return a + b
print(add(2,3))
print(add("h","i"))  # Output: hi, WHY? Because python does not strictly enforce this at runtime
# These methods are mainly for:
# humans reading code
# VS Code autocomplete
# static checkers
# bug prevention
# documentation
# FastAPI / Pydantic later
# large project maintainability
# In backend and AI systems, this becomes extremely important.

def main() -> None:  # None because 'main' does not return useful data, it just perform input, print, run app
    print("Starting system")

# Always try to explain code as much as possible and be specific, for example basic version -
def get_models() -> list:  # Means it will return list
    return ["gpt", "claude", "gemini"]  
# Now the professional version:
def get_models() -> list[str]:  # Means it will return list of string, This is more specific
    return ["gpt", "claude", "gemini"]
# Another example -
def get_available_workspaces() -> list[dict[str, str]]:  
    return [
        {"id": "ws_1", "name": "Personal"},
        {"id": "ws_2", "name": "Startup"},
    ]
# Means it will return a list of dictionaries where each dictionary has string key and string values
# Another example -
def get_user() -> dict[str, str]:  # Means it will return a dictionary where key and value both are string
    return {"name": "Harshit", "role": "AI Engineer"}
# Another example -  # Means Give me a command string, I return a dictionary response with string keys and string values
def process_master_command(user_command: str) -> dict[str, str]: 
    pass

# But suppose the returned dictionary is like, one key's value is string and one is integer then? Then we use '|' or.
def process_master_command(user_command: str) -> dict[str, str | int]: # Like this, str | int
    pass

# NOW, why dict[str, str] is not enough: because right now, the dict contain only 2 sting, but in real life they come mixed
# Instead of "{"status": "error", "message": "unknown command"}" real life something look like: 
# {
#     "status": "success",
#     "workspace_count": 3,
#     "workspaces": ["personal", "startup", "research"]
# }
# They include string, int and list[str] at the same time, so to solve these, we have something.

# 1. Any
from typing import Any  # Any means can be anything
def get_response() -> dict[str, Any]:  # Means keys are strings but values can be anything.
    return {
        "status": "success",
        "workspace_count": 3,
        "workspaces": ["personal", "startup", "research"]
    }
# But it is dangerous when it is overused! Use Any only when the data shape is genuinely mixed or unknown.Do not use Any randomly.

# 2. TypedDict: This is very important for backend style code
from typing import TypedDict
class CommandResponse(TypedDict):  # A CommandResponse dictionary should have status and action.
    status : str
    action : str

def process_master_command(user_command: str) -> CommandResponse:
    return {
        "status": "success",
        "action": "list_workspaces"
    }
# This is cleaner than: def process_master_command(user_command: str) -> dict[str, str]:
# Because TypedDict describes the shape of the dictionary.
# That word matters: shape = what keys exist + what type each value has.

# Problem: success and error responses have different shapes
# Success:
# {
#     "status": "success",
#     "action": "list_workspaces"
# }
# Error:
# {
#     "status": "error",
#     "message": "unknown command"
# }
# They do not have the same keys.

# Professional version -
from typing import TypedDict
class SuccessResponse(TypedDict):
    status : str
    action : str
class ErrorResponse(TypedDict):
    status : str
    action : str
def process_master_command(user_command: str) -> SuccessResponse | ErrorResponse:  # means This function may return either a 
                                                                                   # success response or an error response.
    if user_command == "list workspaces":
        return {
            "status": "success",
            "action": "list_workspaces"
        }

    return {
        "status": "error",
        "message": "unknown command"
    }

# 4. DataClass: Use this when you want to represent structured data as an object.
from dataclasses import dataclass

@dataclass
class Workspace:
    id: str
    name: str
    owner: str
workspace = Workspace(
    id="ws_1",
    name="startup",
    owner="Harshit"
)
print(workspace.name)
# Why useful? Because instead of passing loose dictionaries everywhere:
# {"id": "ws_1", "name": "startup", "owner": "harshit"}
# you create a clear object: Workspace(id="ws_1", name="startup", owner="harshit")
# This is cleaner for configs, workspace models, user objects, AI agent metadata, etc.













# The professional version tells the reader:
# - what the input means
# - what type the input should be
# - what the output shape is
# - what responsibility the function has
# Typing is not decoration. Typing is communication.


