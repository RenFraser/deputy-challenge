from typing import TypedDict


class UserDictType(TypedDict):
    Id: int
    Name: str
    Role: int


class User:
    def __init__(self, user: UserDictType):
        if not isinstance(user['Id'], int) or not isinstance(user['Name'], str) or not isinstance(user['Role'], int):
            raise ValueError("Invalid user input.")

        self.user_id: int = user['Id']
        self.name: str = user['Name']
        self.role: int = user['Role']

    def as_dict(self) -> UserDictType:
        return {
            'Id': self.user_id,
            'Name': self.name,
            'Role': self.role,
        }

