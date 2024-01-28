from rectangle import Rectangle, NegativeValueError
import pytest

@pytest.fixture
def setup1():
    r1 = Rectangle(5)
    return r1

@pytest.fixture
def setup2():
    r2 = Rectangle(3, 4)
    return r2

@pytest.fixture
def setup3():
    r3 = Rectangle(5, 1)
    return r3


def test_wight(setup1):
    assert setup1._width == 5

def test_height(setup2):
    assert setup2._height == 4

def test_perimeter(setup1):
    assert setup1.perimeter() == 20

def test_area(setup2):
    assert setup2.area() == 12

def test_addition(setup2, setup3):
    assert setup2 + setup3 == Rectangle(8, 5.0)

def test_negative_width():
    with pytest.raises(NegativeValueError):
        r = Rectangle(-5)    

def test_negative_height():
    with pytest.raises(NegativeValueError):
        r5 = Rectangle(5, -4)

def test_set_width():
    r6 = Rectangle(5)
    r6.width = 10
    assert r6.width == 10

def test_set_negative_width():
    r7 = Rectangle(5)
    with pytest.raises(NegativeValueError):
        r7.width = -10

def test_set_height():
    r8 = Rectangle(3, 4)
    r8.height = 6 
    assert r8.height == 6 
           
def test_set_negative_height(setup2):
    with pytest.raises(NegativeValueError):
        setup2.height = -6

# def test_subtraction():
#     r9 = Rectangle(10, 1)
#     r10 = Rectangle(3, 4)
#     assert r9 - r10 == Rectangle(13, 5.0)

def test_subtraction_negative_result():
    r11 = Rectangle(3, 4)
    r12 = Rectangle(10, 1)
    with pytest.raises(NegativeValueError):
        r12 - r11

# def test_subtraction_same_perimeter():
#     r13 = Rectangle(5, 1)
#     r14 = Rectangle(4, 3)
#     r15 = r14 - r13
#     assert r15 == Rectangle(0.0)



