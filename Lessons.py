# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)

# for i in range(1, n): 
#     elem = a[i] 
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem

# print('Отсортированный список:', a)

# res = []
# cur_items = {'one': 1}
# res.append(cur_items)
# print(res)


# ATM

# Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# import decimal

# count = 0
# balance = 0

# while True:
#     mode = input('Input an action: 1 - deposit, 2 - withdraw, 3 - exit:  ')
#     if balance > 5_000_000:
#         balance *= 0.9
#     match mode:
#         case '1':
#             withdraw = int(input('Input an withdraw divisible by 50: '))
#             if withdraw % 50 == 0:
#                 balance += withdraw
#                 count += 1
#         case  '2':
#             amount = int(input('Input an amount of money divisible by 50: '))
#             if amount % 50 != 0:
#                 continue
#             comission = amount * 0.015
#             if comission < 30: comission = 30
#             elif comission > 600: comission = 600
#             if balance > (comission + amount):
#                 balance -= (comission + amount)
#                 count += 1
#         case '3':
#             break
#     print(balance)

# if count % 3 == 0:
#     balance *= 1.03




# def merge(list1, list2):
#     list1.extend(list2)
#     return sorted(list1)
# # считываем данные
# numbers1 = [7, 3]
# numbers2 = [0, 4, 2]

# # вызываем функцию
# print(merge(numbers1, numbers2))

# -------------------------------------------------------------------------------

# lesson 4 (function)

# 1

# """Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки."""

# def print_str(text: str) -> None:
#     """Напишите функцию, которая принимает строку текста.
#     Вывести функцией каждое слово с новой строки.
#     ✔ Строки нумеруются начиная с единицы.
#     ✔ Слова выводятся отсортированными согласно кодировки Unicode.
#     ✔ Текст выравнивается по правому краю так, чтобы у самого
#     длинного слова был один пробел между ним и номером строки."""
#     text = text.lower()
#     text = text.split()
#     max_str = len(max(text, key=len))
#     for n, i in enumerate(text, 1):
#         print(f'{n} {i:>{max_str}}')

# s = 'Напишите функцию, которая принимает строку текста.'

# # print_str(s)
# print(print_str.__doc__)


# 2

# """Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию"""

# def get_uni(s: str) -> list[int]:
#     return sorted(list({ord(i) for i in s}), reverse=True)


# s = 'Напишите функцию, которая'
# res = get_uni(s)
# print(res)


# 3

# """Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно"""

# def get_dict(text: str) -> dict[str: int]:
#     start, stop = map(int, text.split())
#     result = {}
#     for i in range(start, stop+1):
#         result[chr(i)] = i
#     return result

# if __name__ == "__main__":
#     print(get_dict('1000 1010'))


# 4

# Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии


# ATM

# Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# import decimal
# MULTIPLICITY = 50
# PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
# MIN_REMOVAL = decimal.Decimal(30)
# MAX_REMOVAL = decimal.Decimal(600)
# PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
# COUNTER4PERCENTAGES = 3
# RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
# RICHNESS_SUM = decimal.Decimal(10_000_000)

# bank_account = decimal.Decimal(0)
# count = 0
# operations = []

# balance = 0

# def check_multiplicity(amount):
#     if amount % MULTIPLICITY == 0:
#         return True
    
# def deposit(amount):
#     global balance
#     if check_multiplicity(amount):
#         balance += amount
#         operations.append(f'Пополнение карты на {amount} у.е. Итого {balance} у.е.')
#     else:
#         print('Сумма должна быть кратной 50 у.е.')


# def withdraw(amount):
#     global balance
#     comission = amount * PERCENT_REMOVAL
#     if comission < MIN_REMOVAL: comission = MIN_REMOVAL
#     elif comission > MAX_REMOVAL: comission = MAX_REMOVAL
#     if check_multiplicity(amount):  
#         if balance >= (comission + amount):
#             balance -= (comission + amount)
#             operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(comission)} у.е.. Итого {int(balance)} у.е.')
#         else:
#             operations.append(f'Недостаточно средств. Сумма с комиссией {comission + amount} у.е. На карте {int(balance)} у.е.')
#     else:
#             operations.append(f'Недостаточно средств. Сумма с комиссией {comission + amount} у.е. На карте {int(balance)} у.е.')
#             print('Сумма должна быть кратной 50 у.е.')


# def exit():
#     global balance
#     if balance > RICHNESS_SUM:
#         tax = balance * RICHNESS_PERCENT
#         balance -= tax
#         operations.append(f'Вычтен налог на богатство 0.1% в сумме {tax} у.е. Итого {balance} у.е.')
#     operations.append(f'Возьмите карту на которой {balance} у.е.')

# deposit(1000000000000000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()

# print(operations)

# --------------------------------------------------------------------------------------

#  Lesson 5

# 1

# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа

# s = '1/2/3/4/7'
# a, b, c, *d = s.split('/')
# result = {b: a, c: tuple(d)}
# print(result)

# 2

# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку

# string = 'aaabbbccc'
# result = {i: ord(i) for i in string}
# print(result)

# dictionary keys are unique


# 3

# Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю

# string = 'aaabcdefg'
# result = {i: ord(i) for i in string}
# my_iter = iter(result.items())
# for _ in range(5):
#     print(next(my_iter))


# 4

# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку

# gen = [i for i in range(0, 101, 2) if sum(int(i) for i in str(i)) != 8]
# print(gen)

# 5

# Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         (print(i))


# print(*['FizzBuzz' if i % 15 == 0 
#        else 'Fizz' if i % 3 == 0 
#        else 'Buzz' if i % 5 == 0 
#        else i for i in range(1, 101)], sep = '\n')


# 6

# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,начиная с числа 2.
# ✔ Для проверки числа на простоту используйтеправило: «число является простым, если делится
# нацело только на единицу и на себя


# def prim(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def gener(n):
#     start = 1
#     counter = 0
#     while counter <= n:
#         start += 1
#         if prim(start):
#             counter += 1
#             yield start

# print(list(gener(10)))
















