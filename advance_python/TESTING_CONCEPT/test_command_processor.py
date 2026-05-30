from command_processor import process_master_command

def test_list_workspace_command() -> None:
    result = process_master_command("list workspaces")

    assert result["status"] == "success"
    assert result["action"] == "list_workspaces"

def test_command_is_case_insensitive() -> None:
    result = process_master_command(" LIST WORKSPACES ")

    assert result["status"] == "success"
    assert result["action"] == "list_workspaces"

def test_unknown_command() -> None:
    result = process_master_command("delete universe")

    assert result["status"] == "error"
    assert result["message"] == "unknown command"

