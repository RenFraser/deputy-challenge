import os
from typing import List
import json
from EmployeeHierarchy import EmployeeHierarchy
from Role import Role, RoleDictType
from User import User, UserDictType


if __name__ == '__main__':

    # These two lines could be refactored to use ConfigParser, where users
    # of the program could pass in their json files upon invocation.
    user_input = os.getcwd() + '/users.json'
    role_input = os.getcwd() + '/roles.json'

    # I've intentionally not handled errors here. If the JSON files are
    # malformed, we don't want a silent failure. For now, the ValueError
    # thrown by json.load() on a malformed json file is sufficient.
    with open(user_input, 'r') as userfile:
        users_json: List[UserDictType] = json.load(userfile)
        users: List[User] = [User(user) for user in users_json]

    with open(role_input, 'r') as rolesfile:
        roles_json: List[RoleDictType] = json.load(rolesfile)
        roles: List[Role] = [Role(role) for role in roles_json]

    hierarchy = EmployeeHierarchy(users, roles)

    print(hierarchy.get_subordinates(1))




