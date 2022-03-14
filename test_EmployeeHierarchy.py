from typing import List

import pytest

from EmployeeHierarchy import EmployeeHierarchy
from Role import Role
from User import User


@pytest.fixture
def users():
    return [
        User({
            "Id": 1,
            "Name": "Adam Admin",
            "Role": 1
        }),
        User({
            "Id": 2,
            "Name": "Emily Employee",
            "Role": 4
        }),
        User({
            "Id": 3,
            "Name": "Sam Supervisor",
            "Role": 3
        }),
        User({
            "Id": 4,
            "Name": "Mary Manager",
            "Role": 2
        }),
        User({
            "Id": 5,
            "Name": "Steve Trainer",
            "Role": 5
        })
    ]


@pytest.fixture
def roles():
    return [
        Role({
            "Id": 1,
            "Name": "System Administrator",
            "Parent": 0
        }),
        Role({
            "Id": 2,
            "Name": "Location Manager",
            "Parent": 1
        }),
        Role({
            "Id": 3,
            "Name": "Supervisor",
            "Parent": 2
        }),
        Role({
            "Id": 4,
            "Name": "Employee",
            "Parent": 3
        }),
        Role({
            "Id": 5,
            "Name": "Trainer",
            "Parent": 3
        })
    ]


# In a production codebase we'd want these names to better reflect the tests
# whilst remaining consistent. We'd likely also want to parameterise this test
# case and include data inputs with bad values, mismatched data inputs and
# various other potential use cases, not just the happy paths. I would not want
# to test the internals, just the public-facing API of the class.
def test_EmployeeHierarchy__get_subordinates_1(users: List[User], roles: List[Role]):
    hierarchy = EmployeeHierarchy(users, roles)
    assert hierarchy.get_subordinates(1) == [
        {"Id": 4, "Name": "Mary Manager", "Role": 2},
        {"Id": 3, "Name": "Sam Supervisor", "Role": 3},
        {"Id": 5, "Name": "Steve Trainer", "Role": 5},
        {"Id": 2, "Name": "Emily Employee", "Role": 4},
    ]


def test_EmployeeHierarchy__get_subordinates_2(users: List[User], roles: List[Role]):
    hierarchy = EmployeeHierarchy(users, roles)
    assert hierarchy.get_subordinates(3) == [
        {"Id": 5, "Name": "Steve Trainer", "Role": 5},
        {"Id": 2, "Name": "Emily Employee", "Role": 4},
    ]
