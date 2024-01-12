# Зачем нужен метод __нью__
# metod __new__ чтобы кастомизировать объекты родительских классов или типы инита флоата
# если вы хотите свой класс, и унаследоваться и смастерить какой то класс, то простым инитом не сможем, 
# нам придется переопределять метод __нью__ чтобы корректно добавить новые атрибуты

"""
Создайте класс Моя Строка, где:
- будут доступны все возможности str
- дополнительно хранятся имя автора строки и время создания (time.time)
"""

import datetime


class MyStr(str):                                       # cls - ссылка на класс, с к-м мы работаем(str)
    """
    Создайте класс Моя Строка, где:
    - будут доступны все возможности str
    - дополнительно хранятся имя автора строки и время создания (time.time).

    >>> MyStr('text', 'Vladislav')
    text
    """
    def __new__(cls, value, author):                    # instance - наш новый экземпляр
        instance = super().__new__(cls, value)          # вызываем метод у родительского класса
        instance.author = author                        # в instance кладем экземпляр класса str
        instance.time = datetime.datetime.now()
        return instance

    def __str__(self):
        return f"{self.author} {self.time}"

if __name__ == '__main__':
    ms1 = MyStr('text', 'Vladislav')
    ms2 = MyStr('new_text', 'Max')
    print(ms1, ms1.author, ms1.time,
          ms2)














