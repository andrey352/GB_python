# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования, дату события, имя функции (не декоратора), аргументы вызова, результат

import logging
from functools import wraps

FORMAT = '%(asctime)s | %(levelname)s | %(message)s'

logging.basicConfig(filename=f'task3_log.log', filemode='a', level=logging.DEBUG, encoding='utf-8', format=FORMAT)

def logging_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.debug(f"Аргументы: {args}|{kwargs}| Результат: {result} | Функция {func.__name__}")
        return result
    return wrapper

@logging_deco
def some_func(a: int|float, b: int|float) -> None | float:
    try:
        return a / b
    except ZeroDivisionError:
        return None

if __name__ == "__main__":
    some_func(1, 2)
    some_func(3, 0)
















