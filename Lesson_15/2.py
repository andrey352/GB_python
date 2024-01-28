# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging

import logging

logging.basicConfig(filename=f'task2_log.log', filemode='a', level=logging.DEBUG, encoding='utf-8')

def logging_deco(func):
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


















