# Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи. Исходный код в 
# редакторе кода надо доработать, чтобы вызывалось исключение NegativeValueError.
# Используйте модуль doctest.
# Тесты:
# test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 
# с отрицательной шириной (-2). Убедимся, что r1.width корректно установлен на 5, а 
# создание r4 вызывает исключение NegativeValueError с текстом Ширина должна быть положительной, а не {value}
# test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 
# с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4. При необходимости 
# выбрасывать исклчение NegativeValueError с текстом Высота должна быть положительной, а не {value}
# test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, 
# что r1.perimeter() возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, 
# что r2.perimeter() возвращает 14.
# test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, 
# что r1.area() возвращает 25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, 
# что r2.area() возвращает 12.
# test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 
# и r2 с шириной 3 и высотой 4. Выполняем операцию сложения r1 + r2 и проверяем, 
# что полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).
# test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и
# r2 с шириной 3 и высотой 4. Выполняем операцию вычитания r1 - r2 и проверяем, 
# что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).
# Запускать тесты не надо, автотест это сделает сам:
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
    """
    >>> r1 = Rectangle(5)

    >>> r4 = Rectangle(-2)
    Traceback (most recent call last):
        ...
    NegativeValueError: Ширина должна быть положительной, а не -2

    >>> r2 = Rectangle(3, 4)
    >>> r2.width == 3
    True
    >>> r2.height == 4
    True
    
    >>> r1 = Rectangle(5)
    >>> r1.perimeter() == 20
    True
    >>> r2 = Rectangle(3, 4)
    >>> r2.perimeter() == 14
    True
    
    >>> r1 = Rectangle(5)
    >>> r1.area() == 25
    True
    >>> r2 = Rectangle(3, 4)
    >>> r2.area() == 12
    True
    
    >>> r1 = Rectangle(5)
    >>> r2 = Rectangle(3, 4)
    >>> r3 = r1 + r2
    >>> r3.width == 8
    True
    >>> r3.height == 9.0
    True
    
    >>> r1 = Rectangle(5)
    >>> r2 = Rectangle(3, 4)
    >>> r3 = r1 - r2
    >>> r3.width == 2
    True
    >>> r3.height == 1
    True
    """

    width = Side()
    height = Side()

    def __init__(self, width, height=None):
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


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) 


    # r1 = Rectangle(5)
    # r2 = Rectangle(3, 4)
    # r3 = r1 - r2
    # print(r3.width)
    # print(r3.height)




