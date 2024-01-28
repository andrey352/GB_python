import pytest
from person import Employee

@pytest.fixture
def setup1():
    p = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    return p

def test_employee_full_name(setup1):
    assert setup1.full_name() == 'Ivanov Ivan Ivanovich'

def test_employee_birthday(setup1):
    setup1.birthday()
    assert setup1.get_age() == 31

def test_employee_raise_salary(setup1):
    setup1.raise_salary(10)
    assert setup1.salary == 55000

def test_employee_str(setup1):
    assert f'{setup1}' == 'Ivanov Ivan Ivanovich (Manager)'

def test_employee_last_name_title(setup1):
    assert setup1.last_name == 'Ivanov'

