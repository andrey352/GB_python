# Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числамииз диапазонов

from typing import Callable
from random import randint

def game(func: Callable) -> Callable[..., any]:
    def wrapper(attempts, puzzle) -> any:
        if not (0 < attempts < 100 and 0 < puzzle < 100):
            attempts = randint(0, 100)
            puzzle = randint(0, 100)
            print('принудительно переданы подходяще аргументы')
        result = func(attempts, puzzle)
        return result
    return wrapper

@game
def guessing(attempts, puzzle) -> bool:
    for i in range(attempts):
        answer = int(input(f'guess the number, you have {attempts - i} attempts:\n'))
        if answer == puzzle: 
            print(f'you have guessed')
            return True
        elif answer > puzzle:
            print('guess number is less')
        else:
            print('guess number is more')
    return False

if __name__ == '__main__':
    guessing(2, 5)                                 # game(guessing)(5, 5)   
















