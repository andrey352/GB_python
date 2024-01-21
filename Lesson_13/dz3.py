# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) 
# имеет следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) 
# Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях 
# (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и 
# генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный 
# идентификационный номер (ID). Класс Employee также должен проверять валидность ID и 
# генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника
# на основе суммы цифр в его ID (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, 
# что исключения работают корректно при передаче неверных данных.
class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, lastname, name, surname, age):
        if not isinstance(lastname, str) or lastname == '':
            raise InvalidNameError(f'Invalid name: {lastname}. Name should be a non-empty string.')
        self.lastname = lastname
        if not isinstance(name, str) or name == '':
            raise InvalidNameError
        self.name = name
        if not isinstance(surname, str) or surname == '':
            raise InvalidNameError
        self.surname = surname
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.lastname} {self.name} {self.surname} {self.age}'
    

class Employee(Person):
    def __init__(self, lastname, name, surname, age, id):
        super().__init__(lastname, name, surname, age)
        if len(str(id)) != 6:
            raise InvalidIdError(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')
        self.id = id

    def get_level(self):
        return sum(map(int, list(str(self.id)))) % 7


# person = Person("", "John", "Doe", 30)
# print()
# Invalid name: . Name should be a non-empty string.

# person = Person("Alice", "Smith", "Johnson", -5)
# print()
# Invalid age: -5. Age should be a positive integer.

# employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
# print()
# Id should be a 6-digit positive integer between 100000 and 999999.












