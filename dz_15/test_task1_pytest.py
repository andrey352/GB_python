
from task1 import Student
import pytest


@pytest.fixture
def setup_1():
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    return student


def test_add_grade(setup_1):
    setup_1.add_grade("Математика", 5)
    assert setup_1.Математика == {'grades': [4, 5], 'test_scores': [85]}

def test_invalid_grade(setup_1):
    with pytest.raises(ValueError):
        setup_1.add_grade("Математика", 11)

def test_add_score(setup_1):
    setup_1.add_test_score("История", 68)
    assert setup_1.История == {'grades': [5], 'test_scores': [92, 68]}

def test_invalid_score(setup_1):
    with pytest.raises(ValueError):
        setup_1.add_test_score("История", -100)    

def test_average_test_score(setup_1):
    setup_1.add_test_score("Математика", 95)
    assert setup_1.get_average_test_score("Математика") == 90.0













