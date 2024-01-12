"""
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""

class Rectangle:
    def __init__(self, height, width=None) -> None:
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def __repr__(self):
        return f"Rectangle({self.height = }, {self.width = })"
        
    def per(self):
        return 2*(self.height + self.width)
    
    def area(self):
        return self.height * self.width
        
    def __add__(self, obj: "Rectangle"):
        new_per = self.per() + obj.per()
        new_height = self.height + obj.height
        new_width = (new_per / 2) - new_height

        if new_width <= 0 or new_height <= 0:
            raise ValueError
        
        return Rectangle(new_height, new_width)

    def __sub__(self, obj: "Rectangle"):
        new_per = self.per() - obj.per()
        new_height = self.height - obj.height
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
    r1 = Rectangle(2, 2)
    r2 = Rectangle(4, 2)
    r3 = Rectangle(1, 4)
    print(r1 == r3)
    print(r1 > r2) 
    print(r1 < r2)
    print(r2 - r1)
    print(r2 + r1)

