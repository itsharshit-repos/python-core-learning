from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    email: str
    plan: str
    credits: int
    is_active: bool

@dataclass
class Workspace:
    id: str
    name: str
    owner_id: str

@dataclass
class Agent:
    id: str
    name: str 
    role: str
    model: str
    workspace_id: str
