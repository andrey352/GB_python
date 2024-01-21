# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError,
# которое выбрасывается при некорректных значениях ширины и высоты, как при
# создании объекта, так и при установке их через сеттеры.

class NegativeValueError(Exception):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} должна быть положительной, а не {self.value}"


class Side:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(self.param_name, value)
        return setattr(instance, self.param_name, value)
    
    def validate(self, name, value):
        if self.param_name == '_width' and value < 0:
            raise NegativeValueError('Ширина', value)
        if self.param_name == '_height' and value < 0:
            raise NegativeValueError('Высота', value)


class Rectangle:

    width = Side()
    height = Side()

    def __init__(self, width, height=None):
        if width < 0:
            raise NegativeValueError('Ширина', width)
        if height != None and height < 0 :
            raise NegativeValueError('Высота', height)
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


r = Rectangle(2)
print(r)
print(r.width)
# __main__.NegativeValueError: Ширина должна быть положительной, а не -2

# r = Rectangle(5, -3)
# __main__.NegativeValueError: Высота должна быть положительной, а не -3

# r = Rectangle(4, 4)
# r.width = -3
# __main__.NegativeValueError: Ширина должна быть положительной, а не -3

# r = Rectangle(4, 4)
# r.height = -3
# __main__.NegativeValueError: Высота должна быть положительной, а не -3



class NegativeValueError(ValueError):
    pass

class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)
