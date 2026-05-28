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

# Default values: You can give defaults
from dataclasses import dataclass
@dataclass
class AIModelConfig:
    model_name: str
    max_tokens: int = 1000
    temperature: float = 0.7
config = AIModelConfig(model_name="demo-ai")
print(config)

# Important trap: LIST AS DEFAULT
# from dataclasses import dataclass
# @dataclass
# class Agent:
#     name : str
#     tools : list[str] = []
# # This is bad, why? Because mutable default list can be shared accidently. Correct one is:
# from dataclasses import dataclass, field
# @dataclass
# class Agent:
#     name: str
#     tools: list[str] = field(default_factory=list)  # This field line means Every agent gets its own fresh tools list.
# This creates a fresh list for every agent.
# Remember this seriously: Mutable defaults are a classic Python bug.

# Important truth: dataclass does not strongly validate types at runtime by default.
# This may still run:
# agent = AgentConfig(
#     name=123,
#     model=True
# )
# Even though you wrote:
# name: str
# model: str
# The type hints help humans, editors, and static checkers.

# DataClass example -
from dataclasses import dataclass
@dataclass
class Workspace:
    id: str
    name: str
    owner: str
    plan: str = "free"
def get_available_workspaces() -> list[Workspace]:
    return [
        Workspace(id="1", name="personal", owner="Harshit"),
        Workspace(id="2", name="startup", owner="Alice", plan="pro"),
        Workspace(id="3", name="research", owner="Bob")
    ]
workspaces = get_available_workspaces()
for workspace in workspaces:
    print(workspace.name)

# This same code in a more professional way:
from dataclasses import dataclass
@dataclass
class Workspace:
    id: str
    name: str
    owner: str
    plan: str = "free"
def get_available_workspaces() -> list[Workspace]:
    return [
        Workspace(id="1", name="personal", owner="Harshit"),
        Workspace(id="2", name="startup", owner="Alice", plan="pro"),
        Workspace(id="3", name="research", owner="Bob")
    ]
def main() -> None:
    workspaces = get_available_workspaces()
    for workspace in workspaces:
        print(workspace.name)
if __name__ == "__main__":
    main()

# One more IMPORTANT dataclass tool is: asdict
# In backend/AI systems, Python objects often need to become dictionaries because JSON/API responses are dictionary-like.
from dataclasses import asdict, dataclass
@dataclass
class Workspace:
    id: str
    name: str
    owner: str
    plan: str = "free"
workspace = Workspace(id="1", name="Startup", owner="Harshit")
print(asdict(workspace))
# Why this matters? Because later in backend/FastAPI, you will often convert internal objects into API responses.
# Mental model:
# dataclass object → internal Python structure
# dict / JSON → external API structure
# So: Workspace(...) is good inside your system. asdict(workspace) is useful when sending data outward.

# 5. Callable: You use Callable when function accept another function. We already saw this indirectly in decorators
from collections.abc import Callable

def run_task(task: Callable[[], None]) -> None:
    print("Starting task..")
    task()
    print("Task finished.")
# 'Callable[[], None]' means function that takes NO arguments and returns None 
def say_hello() -> None:
    print("Hello")
run_task(say_hello)

# Lets take a example for another kind of Callable: 'Callable[[str], str]'
from collections.abc import Callable
def generate_response(prompt: str) -> str:
    return f"Response to: {prompt}"
def run_ai_task(task: Callable[[str], str], prompt: str) -> str: # That Callable[[str], str] means a function that takes one str 
                                                                 # argument and returns a str
    result = task(prompt)
    return result
response = run_ai_task(generate_response, "What is AI?")
print(response)
# Remember this: Callable[[input_types], return_type]

# Callable with multiple arguments: eg. Callable[[int, int], int]
from collections.abc import Callable
def add(a: int, b: int) -> int:
    return a+b
def calculate(operation: Callable[[int, int], int], x: int, y: int) -> int:
    return operation(x,y)
print(calculate(add, 2,3))

# Real AI system example -
from collections.abc import Callable
def search_web(query: str) -> str:
    return f"Searching web for: {query}"
def search_memory(query: str) -> str:
    return f"Searching memory for: {query}"
def run_tool(tool: Callable[[str], str], query: str) -> str:
    return tool(query)
print(run_tool(search_web, "latest AI news"))
print(run_tool(search_memory, "user preferences"))

# Think of Callable like a socket/interface.
# Callable[[str], str]
# means: This socket accepts any function shaped like:
# input: string
# output: string

# This matters for:
# - decorators
# - middleware
# - callbacks
# - background tasks
# - AI tool execution
# - event systems

#----------------------------------------------------------------------------------

# DataClass vs TypedDict

# Use TypedDict when your data is naturally a dictionary, usually for:
# API responses
# JSON-like data
# external data
# command response objects
# Example:
# class ErrorResponse(TypedDict):
#     status: str
#     message: str

# Use dataclass when your data is internal Python state, usually for:
# workspace objects
# agent objects
# model configs
# user sessions
# system settings
# structured application data
# Example:
# @dataclass
# class Agent:
#     id: str
#     name: str
#     model: str

# Simple rule:
# TypedDict = dictionary shape
# dataclass = structured Python object

#---------------------------------------------------------------------------------------------------

# The only strategy we will follow is: 
# Method 1 --------------------------------------------------------------------------------
# Normal type hints, almost uses everywhere
# def generate_response(prompt: str) -> str:
#     return f"AI response for: {prompt}"
# Method 2 --------------------------------------------------------------------------------
# dataclass for structured internal data, when your system has a real object-like thing:
# workspace, user, AI agent, model config, session, tool, project, log event
# from dataclasses import dataclass
# @dataclass
# class Workspace:
#     id: str
#     name: str
#     owner: str
#     plan: str = "free"
# Then:
# def get_workspaces() -> list[Workspace]:
#     return [
#         Workspace(id="1", name="personal", owner="Harshit"),
#         Workspace(id="2", name="startup", owner="Harshit"),
#     ]
# Method 3--------------------------------------------------------------------------------
# Special tools: 1) str | None
# This is optional, means it means return a str if found, else return None
# 2) Callable: Use only when a function receives another function.