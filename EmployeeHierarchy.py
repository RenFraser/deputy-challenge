from typing import List, Dict

from Role import Role
from User import User, UserDictType


class EmployeeHierarchy:
    """Hierarchy of employees by their roles.

    This class implements a tree of roles. In the provided spec, we have
    a few classes, some of which are 'Systems Administrator',
    'Location Manager' and 'Supervisor', where each preceding role is a parent of
    the next. Therefore, the tree would look like this:

    Systems Administrator
            |
      Location Manager
            |
        Supervisor

    If we were to add another child of Location Manager, such as Tech Lead,
    the tree would look like this:

            Systems Administrator
                    |
              Location Manager
                    |
                ---- ----
               |         |
         Supervisor    Tech Lead

    This is represented in the *roles_adjacency_list*, which would be:
    {
        Systems Administrator: [Location Manager],
        Location Manager: [Supervisor, Tech Lead]
    }

    In the code, each role is represented by its unique (see the assumptions
    and design decisions sections of the readme) ID for simplicity.

    For fast lookups, I've mapped role IDs to a list of users that are of that
    role, and I've also mapped each user and role (*users* and *roles*) by
    using a Python dictionary of their IDs to their respective classes.

    This allows me to efficiently traverse the tree in a depth-first-search
    manner.

    """
    def __init__(self, users: List[User], roles: List[Role]):
        self.users: Dict[int, User] = {user.user_id: user for user in users}
        self.roles: Dict[int, Role] = {role.role_id: role for role in roles}

        self.roles_adjacency_list: Dict[int, List[int]] = {}
        self.roles_to_users: Dict[int, List[int]] = {}

        self._rebuild_roles_adjacency_list()
        self._remap_roles_to_users()

    def _rebuild_roles_adjacency_list(self):
        self.roles_adjacency_list = {}

        for role in self.roles.values():
            if role.parent not in self.roles_adjacency_list:
                self.roles_adjacency_list[role.parent] = []

            self.roles_adjacency_list[role.parent].append(role.role_id)

    def _remap_roles_to_users(self):
        self.roles_to_users = {}

        for role in self.roles.values():
            self.roles_to_users[role.role_id] = []

        for user in self.users.values():
            if user.role not in self.roles_to_users:
                self.roles_to_users[user.role] = []

            self.roles_to_users[user.role].append(user.user_id)

    def get_subordinates(self, user_id: int) -> List[UserDictType]:
        """Get all subordinate employees of another, by role.

        This code traverses the roles tree by its adjacency list, finds
        all child nodes of the role that the user with id user_id has and
        looks up all matched users to those roles. The return type is
        List[UserDictType] because the spec has provided examples using
        the JSON object. In reality, we'd really want this guy to have a return
        type of List[User] instead. I'd considered returning the List[User] type
        and later transforming them to type List[UserDictType] (same as the
        input) but felt it was cruft at this point.
        """

        if user_id not in self.users:
            raise ValueError(f"User with id: {user_id} does not exist.")

        subordinates: List[UserDictType] = []

        user: User = self.users[user_id]
        role_ids = []

        stack = []

        # ensure returned subordinates don't include the root employee
        for role_id in self.roles_adjacency_list.get(user.role, []):
            stack.append(role_id)

        while stack:

            # pop the current tree node off the stack and push any children
            current_role_id = stack.pop()
            for role_id in self.roles_adjacency_list.get(current_role_id, []):
                stack.append(role_id)

            role_ids.append(current_role_id)

        # match user ids to the returned roles children, get the corresponding
        # User() classes and transform them to a dict to match the input type
        # from the spec.
        for role_id in role_ids:
            users_with_matching_role_id: List[int] = self.roles_to_users[role_id]

            for user_id in users_with_matching_role_id:
                user_dict: UserDictType = self.users[user_id].as_dict()
                subordinates.append(user_dict)

        return subordinates
