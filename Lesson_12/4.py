# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств

class Rectangle:

    def __init__(self, height, width=None) -> None:
        self._height = height
        if width:
            self._width = width
        else:
            self._width = height

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError
        self._height = value

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError
        self._width = value

    def __repr__(self):
        return f"Rectangle({self._height = }, {self._width = })"
        
    def per(self):
        return 2*(self._height + self._width)
    
    def area(self):
        return self._height * self._width
        
    def __add__(self, obj: "Rectangle"):
        new_per = self.per() + obj.per()
        new_height = self._height + obj._height
        new_width = (new_per / 2) - new_height
        if new_width <= 0 or new_height <= 0:
            raise ValueError
        return Rectangle(new_height, new_width)

    def __sub__(self, obj: "Rectangle"):
        new_per = self.per() - obj.per()
        new_height = self._height - obj._height
        new_width = (new_per / 2) - new_height
        if new_width <= 0 or new_height <= 0:
            raise ValueError
        return Rectangle(new_height, new_width)
    
    def __eq__(self, obj: "Rectangle") -> bool:
        return self.area() == obj.area()

    def __gt__(self, obj: "Rectangle") -> bool:
        return self.area() > obj.area()
    
    def __lt__(self, obj: "Rectangle") -> bool:
        return self.area() < obj.area()


if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r1.width = 10
    print(r1.width)









