# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создани иэкземпляра.
# У класса должно быть два метода, возвращающие периметри площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат

class Rectangle:
    def __init__(self, *args):
        if len(args) == 1:
            self.width, self.length = args[0], args[0]
        else:
            self.width, self.length = args
    
    def get_perimeter(self):
        return (self.width + self.length) * 2
    
    def get_area(self):
        return self.width * self.length
        
if __name__ == "__main__":
    rectangle = Rectangle(3, 6)
    quandrant = Rectangle(5)
    print(f'{rectangle.get_perimeter() = }')
    print(f'{rectangle.get_area() = }')
    print(f'{quandrant.get_perimeter() = }')
    print(f'{quandrant.get_area() = }')
            













