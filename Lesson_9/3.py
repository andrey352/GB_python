# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции

# s = [
#     {
#         'args': [1, 2, 'b'],
#         'b': 1,
#         'c': 'c',
#         'result': 12
#     }
# ]

import json
from typing import Callable

def args_to_json(func) -> Callable[..., any] | None:
    try:
        with open(f'{func.__name__}.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    def wrapper(*args, **kwargs) -> any:
        result = func(*args, **kwargs)
        data.append({'args': args, **kwargs, 'result': result})
        with open(f'{func.__name__}.json', 'w') as file:
            json.dump(data, file, indent=4)

        # return result
    return wrapper

@args_to_json
def do_something(*args, **kwargs) -> str:
    return f'{args} and {kwargs}'

if __name__ == '__main__':
    do_something(1,2,3, a=67, se='h')  

























