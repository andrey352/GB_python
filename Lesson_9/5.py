# Объедините функции из прошлых задач. Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров, ○ декоратором контроля значений и
# ○ декоратором для многократного запуска. Выберите верный порядок декораторов.

from random import randint
import json
from functools import wraps


def count(repeats: int):
    def deco(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('go 3')
            result = []
            for _ in range(repeats):
                print('go 3.1')
                result.append(func(*args, **kwargs))
                print(f'{result}, "go 3"')
            print('go 3.2')
            return result
        return wrapper
    return deco


def args_to_json(func):
    try:
        with open(f'{func.__name__}.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        print('go 2')
        result = func(*args, **kwargs)
        data.append({'args': args, **kwargs, 'result': result})
        with open(f'{func.__name__}.json', 'w') as file:
            json.dump(data, file, indent=4)
        return result
    return wrapper


def game(func: callable):
    @wraps(func)
    def wrapper(attempts, puzzle) -> any:
        if not (0 < attempts < 100 and 0 < puzzle < 100):
            attempts = randint(0, 100)
            puzzle = randint(0, 100)
            print('принудительно переданы подходящие аргументы')
        print('go 1')
        result = func(attempts, puzzle)
        return result
    return wrapper

@count(2)
@args_to_json
@game
def guessing(attempts, puzzle) -> None:
    for i in range(attempts):
        answer = int(input(f'guess the number, you have {attempts - i} attempts: '))
        if answer == puzzle: 
            print(f'you have guessed')
            return True
        elif answer > puzzle:
            print('guess number is less')
        else:
            print('guess number is more')
    return False


if __name__=='__main__':
    guessing(3, 4)






























