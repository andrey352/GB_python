# Возьмите код из прошлой задачи "Управление информацией о сотрудниках и их возрасте".
# Ваша задача - написать набор тестов для класса Employee, чтобы убедиться, что он работает правильно.
# Тесты должны быть написаны с использованием модуля unittest и лежать в class TestEmployee(unittest.TestCase).
# Тесты:
# test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", 
# именем "Ivan", отчеством "Ivanovich" и убедитесь, что метод full_name() возвращает правильное полное имя
# в формате "Ivanov Ivan Ivanovich".
# test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с возрастом 30, 
# вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.
# test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000,
# вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.
# test_employee_str: Тестирование метода __str__(). Создайте объект Employee с данными: фамилия "Ivanov", 
# имя "Ivan", отчество "Ivanovich", возраст 30, должность "manager" и зарплата 50000. Убедитесь, что метод
# __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".
# test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией
# "Ivanov" и убедитесь, что атрибут last_name не возвращает в верхнем регистре "Ivan".
import unittest
from person import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.p = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)

    def test_employee_full_name(self):
        self.assertEqual(self.p.full_name(), 'Ivanov Ivan Ivanovich')

    def test_employee_birthday(self):
        self.p.birthday()
        self.assertEqual(self.p.get_age(), 31)

    def test_employee_raise_salary(self):
        self.p.raise_salary(10)
        self.assertEqual(self.p.salary, 55000)

    def test_employee_str(self):
        self.assertEqual(f'{self.p}', 'Ivanov Ivan Ivanovich (Manager)')

    def test_employee_last_name_title(self):
        self.assertNotEqual(self.p.last_name, 'ivan')

if __name__ == "__main__":
    unittest.main(verbosity=4)




















