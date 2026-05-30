# AI System style example -

# This is command_processor.py
from typing import TypedDict

class SuccessResponse(TypedDict):
    status: str
    action: str
class ErrorResponse(TypedDict):
    status: str
    message: str

def process_master_command(user_command: str) -> SuccessResponse | ErrorResponse:
    command = user_command.lower().strip()

    if command == "list workspaces":
        return {
            "status": "success",
            "action": "list_workspaces"
        }
    return {
        "status": "error",
        "message": "unknown command"
    }