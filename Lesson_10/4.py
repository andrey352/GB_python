# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания. У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

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
    

class Employee(Person):
    def __init__(self, first_name, second_name, last_name, age: int, id: int):
        super().__init__(first_name, second_name, last_name, age)
        self.id = int(f'{id:<06}')
        self.level = sum(map(int, str(self.id))) % 7



if __name__ == '__main__':
    p1 = Person('Bauer', 'Andrey', 'Viktorovich', 34)
    p1.birthday()
    print(p1.current_age())
    print(p1.full_name())
    e1 = Employee('Bauer', 'Andrey', 'Viktorovich', 34, 111)
    print(e1.level)
    print(e1.id)
    print(e1.current_age())





















