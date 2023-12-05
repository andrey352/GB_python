#  Lesson 6

# 1

# Создайте модуль с функцией внутри.
# 📌 Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# 📌 Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное числопопыток.
# 📌 Функция выводит подсказки “больше” и “меньше”.
# 📌 Если число угадано, возвращается истина, а если попытки исчерпаны - ложь

# 2

# Улучшаем задачу 2.
# 📌 Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# 📌 Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# 📌 Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное выражение

__all__ = ["enigma"]


from random import randint
from sys import argv

def enigma(start: int, stop: int, attpts: int) -> bool:
    digit = randint(start, stop)
    for _ in range(attpts):
        guess = int(input('Guess a number: '))
        if guess == digit:
            return True
        elif guess < digit:
            print('digit is more than your number')
        else:
            print('digit is less than your number')
    else:
        print('attempts are exhausted')
        return False

if __name__ == "__main__":
    _, start, stop, attempts = argv
    print(enigma(int(start), int(stop), int(attempts)))















