# Write tests for:
# 1. get_available_workspaces returns 3 workspaces
# 2. first workspace name is personal
# 3. find_workspace("startup") returns a Workspace
# 4. find_workspace("gaming") returns None
# 5. startup workspace plan is pro

# Use plain pytest style:
# def test_something() -> None:
#     assert ...

# Run: pytest

from workspace_service import get_available_workspaces, find_workspace, Workspace, get_workspace_names

# 1. get_available_workspaces returns 3 workspaces
def test_get_available_workspace_count() -> None:
    workspaces = get_available_workspaces()
    assert len(workspaces) == 3

# 2. first workspace name is personal
def  test_first_workspace_name_is_personal() -> None:
    workspaces = get_available_workspaces()
    assert workspaces[0].name == "personal"

# 3. find_workspace("startup") returns a Workspace
def test_find_workspace_startup_returns_object() -> None:
    result = find_workspace("startup")
    assert isinstance(result, Workspace)
    assert result.name == "startup"

# 4. find_workspace("gaming") returns None
def test_find_workspace_gaming_returns_none() -> None:
    result = find_workspace("gaming")
    assert result is None

# 5. startup workspace plan is pro
def test_startup_workspace_plan_is_pro() -> None:
    result = find_workspace("startup")
    assert result is not None
    assert result.plan == "pro"

def test_get_workspace_names() -> None:
    assert get_workspace_names() == ["personal", "startup", "research"]