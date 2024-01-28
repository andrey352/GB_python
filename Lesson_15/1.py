# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль
import logging

logging.basicConfig(filename=f'{__name__}_errors.log', filemode='a', level=logging.ERROR, encoding='utf-8')



def some_func(a: int|float, b: int|float) -> None | float:
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"При аргументах {a} {b} возникла {e}")
        return None

if __name__ == "__main__":
    some_func(1, 2)
    some_func(3, 0)













