# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json

class User:
    def __init__(self, name: str, id: int, level: int):
        self.id = id
        self.name = name
        self.level = level


def load_users(filename: str = "users.json") -> set[User]:
    with open("users.json", 'r') as source:
        data = json.load(source)
    return set(map(lambda x: User(**x), data))       # User(id=id, name=name, level=level)


if __name__ == "__main__":
    print(load_users())









