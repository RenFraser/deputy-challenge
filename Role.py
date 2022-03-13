from typing import TypedDict


class RoleDictType(TypedDict):
    Id: int
    Name: str
    Parent: int


class Role:
    def __init__(self, role: RoleDictType):
        if not isinstance(role['Id'], int) or not isinstance(role['Name'], str) or not isinstance(role['Parent'], int):
            raise ValueError("Invalid role input.")

        self.role_id: int = role['Id']
        self.name: str = role['Name']
        self.parent: int = role['Parent']
