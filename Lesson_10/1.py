# import time

# class Test:                                           # __init__ это метод

#     degree  = 2                                       # degree - свойство класса(будут одинаковы для всех экз-ров)

#     def __init__(self, x, y):                                # self - ссылка на экземпляр
#         self.gypot = (x**self.degree + y**self.degree)**0.5  # переменная в init - атрибут(может быть уникальным)  

# t1 = Test(3, 4)                                         # t1 - экземпляр класса
# print(t1.gypot)

# когда мы пишем "переменная" = "класс"  мы вызываем инит
# gipot - атhибут уровня экземпляра класса, класс к ним доступа не имеет




# Создайте класс окружность.
# Класс должен принимать радиус окружности при создани иэкземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь

from math import pi

class Circle:
    _pi = pi

    def __init__(self, radius) -> None:                       # инит это конструктор
        self.radius = radius

    def get_circle_length(self):
        return self.radius * self._pi * 2
    
    def get_circle_area(self):
        return (self._pi * self.radius)**2


if __name__ == '__main__':
    circle = Circle(3)
    print(f"{circle.get_circle_length() = }")
    print(f"{circle.get_circle_area() = }")














