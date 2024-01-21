# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(3)
        self.r2 = Rectangle(3)

    def test_rectangle_creation_one_side(self):
        self.assertIsNotNone(self.r1._width, f"Проверьте инициализацию ширины если передана только высота")
        self.assertEqual(self.r1._width, 3)

    def test_rectangle_creation_negative_side(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, -3)

    def test_sum_rectangles_is_rectangle(self):
        self.assertIsInstance(self.r1 + self.r2, Rectangle, "Проверьте что результат сложения - Rectangle")

if __name__ == "__main__":
    unittest.main(verbosity=4)




















