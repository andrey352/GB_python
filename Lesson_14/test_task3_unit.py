# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов(кроме п. 1)

import unittest
from task2 import clear_text

class TestClearTest(unittest.TestCase):
    def test_no_changes(self):
        self.assertEqual(clear_text("Привет мир"), 'привет мир')

    def test_register_change(self):
        base_text = "привет мир"
        test_strings = {base_text.replace(symbol, symbol.upper()) for symbol in base_text}
        for test_str in test_strings:
            self.assertEqual(clear_text(test_str), 'привет мир')
    
    def test_punktuation_delete(self):
        self.assertEqual(clear_text("Привет. мир!!!"), 'привет мир')

    def test_foreign_alphabets(self):
        self.assertEqual(clear_text("ПриветHello мир"), 'привет мир')

    def test_all_condition(self):
        self.assertEqual(clear_text("ПриветHello миР123..."), 'привет мир')


if __name__ == "__main__":
    unittest.main(verbosity=4)


















