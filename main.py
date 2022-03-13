import os
from typing import List
import json
from EmployeeHierarchy import EmployeeHierarchy
from Role import Role, RoleDictType
from User import User, UserDictType


if __name__ == '__main__':

    user_input = os.getcwd() + '/users.json'
    role_input = os.getcwd() + '/roles.json'

    with open(user_input, 'r') as userfile:
        users_json: List[UserDictType] = json.load(userfile)
        users: List[User] = [User(user) for user in users_json]

    with open(role_input, 'r') as rolesfile:
        roles_json: List[RoleDictType] = json.load(rolesfile)
        roles: List[Role] = [Role(role) for role in roles_json]

    hierarchy = EmployeeHierarchy(users, roles)

    print(hierarchy.get_subordinates(1))




