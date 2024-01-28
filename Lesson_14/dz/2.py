# Возьмите код из прошлой задачи "Класс Rectangle".
# Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)
# Тесты:
# test_width: Тестирование инициализации ширины. Создайте прямоугольник с шириной 5 и убедитесь, 
# что атрибут width корректно установлен на 5.
# test_height: Тестирование инициализации ширины и высоты. Создайте прямоугольник с шириной 3 
# и высотой 4 и убедитесь, что атрибут height корректно установлен на 4.
# test_perimeter: Тестирование вычисления периметра. Создайте прямоугольник с шириной 5 и 
# вычислите его периметр. Убедитесь, что результат равен 20.
# test_area: Тестирование вычисления площади. Создайте прямоугольник с шириной 3 и высотой 4 
# и вычислите его площадь. Убедитесь, что результат равен 12.
# test_addition: Тестирование операции сложения. Создайте два прямоугольника: один с шириной 5, 
# другой с шириной 3 и высотой 4. Выполните операцию сложения r1 + r2 и убедитесь, 
# что полученный прямоугольник имеет правильные значения ширины и высоты (8 и 6.0 соответственно).
# Используйте модуль unittest для запуска тестов. Все тесты должны выполняться успешно и не вызывать ошибок.
from rectangle import Rectangle
import unittest

class TestRect(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(3, 4)

    def test_wight(self):
        self.assertEqual(self.r1._width, 5)

    def test_height(self):
        self.assertEqual(self.r2._height, 4)

    def test_perimeter(self):
        self.assertEqual(self.r1.per(), 20)

    def test_area(self):
        self.assertEqual(self.r2.area(), 12)

    def test_addition(self):
        self.assertEqual(self.r1 + self.r2, Rectangle(8, 6.0))

  
if __name__ == "__main__":
    unittest.main(verbosity=4)










