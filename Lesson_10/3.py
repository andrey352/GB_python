# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Person:
    def __init__(self, first_name, second_name, last_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f"{self.first_name} {self.second_name} {self.last_name} {self.__age}"
    
    def current_age(self):
        return self.__age
    
    @staticmethod
    def say_hello():
        return 'Hello world!'
    

if __name__ == '__main__':
    p1 = Person('Bauer', 'Andrey', 'Viktorovich', 34)
    p1.birthday()
    print(p1.current_age())
    print(p1.full_name())
    p1.__age = 3
    print(p1.current_age())
    print(p1.say_hello())
    print(Person.say_hello())



















