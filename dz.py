


# s = (1, 2, 3, '2', 3.2, True)
# dic = {}
# for i in s:
#     dic[type(i)] = dic.get(type(i), []) + [i]
# print(dic)

# s = [1, 2, 3, 3, 3, 3, 4, 1]
# for i in s:
#     repit = s.count(i)
#     if repit % 2 == 0:
#         for _ in range(repit):
#             s.remove(i)
# print(s)

# сформируйте список с порядоквыми номерами нечетных чисел. Нумерация с еденицы

# s = [1, 2, 7, 4, 5, 5, 1]
# d = []
# for i, el in enumerate(s, 1):
#     if el % 2 != 0:
#         d.append(i)
# print(d)

# s = 'Пользователь вводит строку текста, \
#      Вывести каждое слово'
# s = s.split()
# s.sort()

# max_len = len(max(s, key=len))
# print(max_len, max(s, key=len))
# for i, word in enumerate(s, 1):
#     print(f'{i} {word:>{max_len}}')

# s = 'Пользователь вводит строку текста'
# dir = {}
# for i in s.lower().replace(' ', ''):
#     dir[i] = dir.get(i, 0) + 1
# print(dir)

# dic = {
#     'Aaz' : ('спички', 'спальник', 'дрова', 'топор'),
#     'Steev': ('спальник', 'спички', 'вода', 'еда'),
#     'Tananda': ('вода', 'спички', 'косметичка')
# }

# temp = None
# for things in dic.values():
#     if not temp:
#         temp = set(things)
#         continue
#     temp = temp.intersection(set(things))
# print(temp)

# res = {}
# for name, things in dic.items():
#     temp = set(things)
#     temp_o = set()
#     for other in dic.values():
#         if things == other:
#             continue
#         temp_o = temp_o.union(set(other))
#     temp = temp.difference(temp_o)
#     if temp:
#         res.update({name: temp})
# print(res)


# res_miss = {}
# for name, things in dic.items():
#     temp = set(things)
#     for other in dic.values():
#         if things == other:
#             continue
#         temp_o = temp_o.intersection(set(other))
#     temp = temp.difference(temp_o)
#     if temp:
#         res_miss.update({name: temp})
# print(res_miss)


# dz_3


# 1

# На вход подается словарь со списком вещей для похода в качестве ключа 
# и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.

# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
# sum = 0
# backpack = {}
# for name, weight in items.items():
#     sum += weight
#     backpack.update({name: weight})
#     if sum > 1:
#         break
# backpack.popitem()
# print(backpack)


# 2

# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания
# и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как 
# убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем. Отсортируйте по убыванию значения количества повторяющихся слов. 

# text = "Python 3.9 is the latest version of Python. It's awesome!"
# text = text.replace('.', ' ')
# text = text.replace(',', ' ')
# text = text.replace("'", ' ')
# text = text.replace('!', ' ')
# print(text)
# text = text.lower().split()

# text = [i for i in text if not i.isdigit()]

# dic = {}
# sort_dic = []

# for word in text:
#     dic[word] = dic.get(word, 0) + 1

# sort_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
# print(sort_dic[:10])


# 4

# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

# lst = [1, 1, 2, 2, 3, 3]
# s = []
# for i in lst:
#     if lst.count(i) > 1:
#         s.append(i)
# print(list(set(s)))


# 3

# На вход подается словарь со списком вещей для похода 
# в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.
# В переменную result выведите список, содержащий все возможные варианты backpack. 
# Напечатайте переменную result.
# *Верните все возможные варианты комплектации рюкзака.

# def fill_b(items, max_weight, cur_weight, cur_items, res):
#     for item, weight in items.items():
#         if cur_weight + weight <= max_weight:
#             cur_items[item] = weight
#             cur_weight += weight
#             if cur_weight == max_weight:
#                 res.append(dict(cur_items))
#             else:
#                 fill_b(items, max_weight, cur_weight, cur_items, res)
#             del cur_items[item]
#             cur_weight -= weight

# def main():
#     items = {
#         "ключи": 0.3,
#         "кошелек": 0.2,
#         "телефон": 0.5,
#         "зажигалка": 0.1
#     }
#     max_weight = 1.0

#     res = []
#     fill_b(items, max_weight, 0, {}, res)
#     for i in res:
#         print(i)

# main()



# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0

# cur_weight = 0
# cur_items = {}
# res = {}

# for item, weight in items.items():
#     if cur_weight + weight <= max_weight:
#         cur_items[item] = weight
#         cur_weight += weight
#         if cur_weight == max_weight:
#             res.append(dict(cur_items))
#         else:
#             fill_b(items, max_weight, cur_weight, cur_items, res)
#         del cur_items[item]
#         cur_weight -= weight


# dz_4


# 1

# Напишите функцию для транспонирования матрицы transposed_matrix,
#  принимает в аргументы matrix, и возвращает транспонированную матрицу. 

# def transpose(mtx: list[list]) -> list[list]:
#     s = [[0 for j in range(len(mtx))] for i in range(len(mtx[0]))]
#     for i in range(len(mtx)):
#         for j in range(len(mtx[0])):
#             s[j][i] = mtx[i][j]
#     return s

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# transposed_matrix = transpose(matrix)
# print(transposed_matrix)


# 2

# Напишите функцию key_params, принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ 
# - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление. 

# def key_params(**kwargs) -> dict:
#     s = {}
#     for key, value in kwargs.items():
#         if str(value).isdigit():
#             s[value] = key
#         elif type(value) == dict:
#             s[str(value)] = key
#         elif '.' in str(value):
#             str(value).replace('.', '')
#             s[value] = key
#         elif type(value) == bool:
#             s[value] = key
#         else:
#             s[str(value)] = key
#     return s

# params = key_params(name = 'Alice', age = 30, scores = [85, 90, 78], 
        #    info = {'city': 'New York', 'email': 'alice@example.com'})
# print(params)


# {'Alice': 'name', 30: 'age', '[85, 90, 78]': 'scores',
#  "{'city': 'New York', 'email': 'alice@example.com'}": 'info'}


# 3

# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, 
# выполняя следующие операции, для выполнения которых необходимо написать следующие функции:
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях. 
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

# def deposit(amount):
    

# ---------------------------------------------------------------------------

#  dz_5

# 1

# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла
# ('C:/Users/User/Documents/', 'example', '.txt')     - output

# file_path = '/home/user/docs/my.file.with.dots.txt'
# ('/home/user/docs/', 'my.file.with.dots', '.txt')

# file_path = '/home/user/data/file'
# ('/home/user/data/', '', '.file')

# file_path = 'C:/Users/User/Documents/example.txt'
# ('C:/Users/User/Documents/', 'example', '.txt')

# file_path = 'D:/myfile.txt'
# ('D:/', 'myfile', '.txt')

# file_path = 'C:/Projects/project1/code/script.py'
# ('C:/Projects/project1/code/', 'script', '.py')

# file_path = 'file_in_current_directory.txt'
# ('', 'file_in_current_directory', '.txt')

# def get_file_info(file_path):
#     s = file_path
#     *_, b = s.split('/')
#     ind = b.index('.')
#     name = b[:ind]
#     ext = b[ind:]
#     path = s[:s.index(name)]
#     return (path, name, ext)
# print(get_file_info(file_path = 'C:/Projects/project1/code/script.py'))

# def get_file_info(file_path):
#     s = file_path
#     *_, b = s.split('/')
#     if s.count('.') == 1:
#         ind = b.index('.')
#         name = b[:ind]
#         ext = b[ind:]
#         path = s[:s.index(name)]
#     else:
#         if s.count('.') == 0:
#             ext = '.' + b
#             name = ''
#             ind = s.index(b)
#             path = s[:ind]
#         else:
#             c = b
#             c = c.split('.')
#             ext = '.' + c[-1]
#             ind = b.index(c[-1])
#             name = b[:ind-1]
#             path = s[:s.index(name)]
#     return (path, name, ext)     
# print(get_file_info(file_path = '/home/user/data/file'))

# 2

# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии. 

# def bon(names, salary, bonus):
#     z = zip(names, salary, bonus)
#     return {a: b * int(c[:-1])/100 for a, b, c in z}

# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]

# print(bon(names, salary, bonus))


# 3

# Создайте функцию генератор чисел Фибоначчи fibonacci.
# 0 1 1 2 3 5 8 13

# def fibonacci():

#     yield 0
#     yield 1
#     yield 1
#     a = 1
#     b = 1
#     for _ in range(20):
#         a, b = b, a + b
#         yield b

# f = fibonacci()
# for i in range(10):
#     print(next(f))


# ---------------------------------------------------------------------------

#  dz_6

# 1

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# __all__ = ["is_date_valid"]

# __DAYS_IN_MONTH = {
#     1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
# }

# def is_date_valid(date: str) -> bool:
#     day, month, year = [int(i) for i in date.split('.')]
#     return 1 <= year <= 9999 and 1 <= month <= 12 and __day_valid(day, month, year)

# def __day_valid(day, month, year) -> bool:
#     if __is_leap_year(year) and month == 2:
#         return 1 <= day <= 29
#     return 1 <= day <= __DAYS_IN_MONTH[month]

# def __is_leap_year(year) -> bool:
#     return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# if __name__ == '__main__':
#     print(is_date_valid("29.02.2023"))


# 2

# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens), 
# которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.

# def is_fight(q):
#     for i in range(len(q)):
#         for j in range(len(q)):
#             if i == j:
#                 continue
#             if abs(q[j][0] - q[i][0]) == abs(q[j][1] - q[i][1]) or q[i][0] == q[j][0] or q[j][1] == q[i][1]:
#                 return False
#     return True

# q = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] 

# print(is_fight(q))


# 3

# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей 
# на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким 
# образом, что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо. 

# from random import randint

# def is_fight(q):
#     for i in range(len(q)):
#         for j in range(len(q)):
#             if i == j:
#                 continue
#             if abs(q[j][0] - q[i][0]) == abs(q[j][1] - q[i][1]) or q[i][0] == q[j][0] or
#                 q[j][1] == q[i][1]:
#                 return False
#     return True

# def generate_boards():
#     res = []
#     while True:
#         s = []
#         for i in range(8):
#             a, b = randint(1, 8), randint(1, 8)
#             s.append((a, b))
#         if is_fight(s):
#             res.append(s)
#             print(res)
#             if len(res) == 4:
#                 return res

# print(generate_boards())

# ---------------------------------------------------------------------------

#  dz_7

# 1

# эталонное решение:

# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного 
# имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

# import os
# import shutil

# # Создать тестовую папку
# folder_name = "test_folder"
# folder_path = os.path.join(os.getcwd(), folder_name)
# if os.path.exists(folder_path):
#     shutil.rmtree(folder_path)
# os.makedirs(folder_path)

# # Заполнить тестовую папку
# file_name = "test1.txt"
# file_path = os.path.join(folder_path, file_name)
# with open(file_path, "w") as file:
#     file.write("This is a test file.\n")
#     file.close()


# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []

#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')
#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]

#     # Сортируем файлы по имени
#     filtered_files.sort()

#     # # Задаем начальный номер для порядкового номера
#     num = 1

#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]

#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]

#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)

#         # Увеличиваем порядковый номер
#         num += 1

# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")



# мое решение:

# from pathlib import Path
# import os

# def rename_files(desired_name, num_digits, source_ext, target_ext):
#     os.chdir('..')
#     directory = Path.cwd()
#     count = 1
#     for file in directory.iterdir():
#         if file.suffix == '.' + source_ext:
#             num = str(count).zfill(num_digits)
#             new_name = Path(f'{desired_name}{num}.{target_ext}')
#             file.rename(new_name)
#             count += 1


# ---------------------------------------------------------------------------

#  dz_8

# 1

# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит
# эту директорию и все вложенные директории. Результаты обхода должны быть сохранены
# в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:
# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: 
# Это файл или директория. Размер: Для файлов - размер в байтах, для директорий - размер,
# учитывая все вложенные файлы и директории в байтах. Важные детали:
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Для файлов сохраните их размер в байтах.
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри 
# данной директории, и вложенных директорий.
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. 
# Форматы файлов должны быть выбираемыми.
# Для обхода файловой системы вы можете использовать модуль os.
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход
# директории и возвращать результаты в виде списка словарей. После этого результаты должны быть 
# сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций 
# save_results_to_json, save_results_to_csv и save_results_to_pickle.

# my decision

# import os
# import json, csv, pickle
# from pathlib import Path

# res = []

# def traverse_directory(directory):
#     tree = os.walk(directory)
#     for address, dirs, files in tree:
#         for i in dirs+files:
#             path = os.path.join(address, i)     # absol path - (Path.cwd(), address, i) 
#             size = os.path.getsize(path)
#             if '.' in i: 
#                 type = 'file'
#             else: type = 'Directory'
#             res.append({'Path':path, 'Type':type, 'Size':size})
#     print(res)
#     save_results_to_json(res)
#     save_results_to_csv(res)
#     save_results_to_pickle(res)


# def save_results_to_json(res):
#     with open('json_dz.json', 'w') as otp:
#         json.dump(res, otp, indent=4)

# def save_results_to_csv(res):
#     with open('csv_dz.csv', 'w') as otp:
#         writer = csv.DictWriter(otp, ['Path', 'Type', 'Size'])
#         writer.writeheader()
#         writer.writerows(res)

# def save_results_to_pickle(res):
#     with open('pickle_dz.pickle', 'bw') as otp:
#         pickle.dump(res, otp)


# if __name__ == '__main__':
#     traverse_directory('Lesson_8')



# эталонное решение

# import os
# import json
# import csv
# import pickle


# def get_dir_size(start_path='.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         print(dirpath, dirnames, filenames)
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#         for d in dirnames:
#             dp = os.path.join(dirpath, d)
#             total_size += get_dir_size(dp)
#     return total_size

# def save_results_to_json(results, file_name):
#     with open(file_name, 'w') as f:
#         json.dump(results, f)


# def save_results_to_csv(results, file_name):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Path', 'Type', 'Size'])
#         for result in results:
#             writer.writerow([result['Path'], result['Type'], result['Size']])


# def save_results_to_pickle(results, file_name):
#     with open(file_name, 'wb') as f:
#         pickle.dump(results, f)


# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             size = os.path.getsize(path)
#             results.append({'Path': path, 'Type': 'File', 'Size': size})
#         for name in dirs:
#             path = os.path.join(root, name)
#             size = get_dir_size(path)
#             results.append({'Path': path, 'Type': 'Directory', 'Size': size})
#     return results


# traverse_directory('Lesson_8')


















