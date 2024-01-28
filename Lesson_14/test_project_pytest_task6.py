from project import Project
from exceptions import ProjectAccessException, ProjectLevelException
from users_module import User
import pytest

@pytest.fixture
def setup_for_adding_users():
    p1 = Project()
    p1.auth("vlad", 11)
    return p1

@pytest.fixture
def setup_for_auth():
    p1 = Project()
    return p1


def test_auth_valid_data(setup_for_auth):
    setup_for_auth.auth("vlad", 11)
    assert setup_for_auth.admin == User("vlad", 11, None)

def test_auth_invalid_data(setup_for_auth):
    with pytest.raises(ProjectAccessException):
        setup_for_auth.auth("vlaaaaaad", 0000)

def test_add_correct_user(setup_for_adding_users):
    setup_for_adding_users.add_new_user('Taylor', 666, 5)
    assert User('Taylor', 666, 5) in setup_for_adding_users.users


def test_add_invalid_user(setup_for_adding_users):
    with pytest.raises(ProjectLevelException):
        setup_for_adding_users.add_new_user('Taylor', 666, 1)





