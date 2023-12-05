# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции

import random

def count(repeats: int):
    def deco(func: callable):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(repeats):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return deco

@count(5)
def do_something(*args, **kwargs):
    return random.randint(1, 100)

if __name__ == '__main__':
    print(do_something(1, 2, 3, name=3))
    




























