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
        Workspace(id="2", name="startup", owner="Harshit", plan="pro"),
        Workspace(id="3", name="research", owner="Harshit"),
    ]

def find_workspace(name: str) -> Workspace | None:
    workspaces = get_available_workspaces()

    for workspace in workspaces:
        if workspace.name == name:
            return workspace
    return None

def get_workspace_names() -> list[str]:
    workspaces = get_available_workspaces()
    name_list = []
    for workspace in workspaces:
        name_list.append(workspace.name)
    return name_list
print(get_workspace_names())