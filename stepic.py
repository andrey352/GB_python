# import json
# import csv

# subs = {
#     'Математика':{
#         'grades':[2, 2, 3],
#         'tests':[90, 80, 90]
#     },
#     'История':{
#         'grades':[4, 5, 5],
#         'tests':[50, 30, 40]
#     }
# }


# with open('my_json.json', 'w', encoding='utf-8') as src:
#     json.dump(subs, src)

# with open('my_json.json', 'r', encoding='utf-8') as src:
#     data = json.load(src)
#     data = [{'sub': sub, **perfs} for sub, perfs in data.items()]
    # print(data)

# with open('my_csv.csv', 'w', encoding='utf-8') as otp:
#     writer = csv.DictWriter(otp, ['sub', 'grades', 'tests'])
#     writer.writeheader()
#     writer.writerows(data)

# with open('my_csv.csv', 'r') as src:
#     reader = csv.reader(src)
#     for row in reader:
#         print(row)


# with open('my_csv.csv', 'r') as trgt:
#     data = csv.DictReader(trgt)

# if __name__ == '__main__':
#     for i in data:
#         print(i)

# res['Математика']['grades'].append(5)
# print(res['Математика']['grades'])

# a = list(res.keys())
# for i in a:
#     print(i)



# import random

# a = random.randint(1, 100)
# print('Добро пожаловать в числовую угадайку')

# def is_valid(n):
#     return n.isdigit() and  1 <= int(n) <= 100

# def input_num():
#     while True:
#         n = input('input a number: ')
#         if not is_valid(n):
#             return print('А может быть все-таки введем целое число от 1 до 100?')
#         else:
#             return int(n)

# def compare_num():
#     count = 0
#     choose = 'd'
#     while choose == 'd':
#         n = input_num()
#         if n < a:
#             print('Ваше число меньше загаданного, попробуйте еще разок')
#             count += 1
#         elif n > a:
#             print('Ваше число больше загаданного, попробуйте еще разок')
#             count += 1
#         else:
#             count += 1
#             print(f'Вы угадали, поздравляем!, кол-во попыток - {count}')
#             choose = input('если хотите еще, введите - "d", если нет - "n"')
#             if choose != 'd':
#                 break
#             else:
#                 count = 0

# compare_num()


    # eng_lower = 'abcdefghijklmnopqrstuvwxyz'
    # eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    # rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    # symbol = [" ", ",", ".", "!", "?"]

    # print("Выберите язык: aнгл=e, рус=r")
    # lan = input()
    # print("Выберите шифрование: шифрование - ch, дешифрование - def")
    # chif = input()
    # print("Введите ключ шифрования")
    # n = int(input())
    # print("Введите фразу")
    # f = input()
    # res = ''

    # if chif == 'def':
    #     n = -n
    # if lan == 'e':
    #     mod = 26
    # else:
    #     mod = 32

    # for i in range(len(f)):
    #     if f[i].isalpha():
    #         if lan == 'e':
    #             if f[i].isupper():
    #                 res += eng_upper[((eng_upper.find(f[i]) + n) % mod)]
    #             else:
    #                 res += eng_lower[((eng_lower.find(f[i]) + n) % mod)]
    #         else:
    #             if f[i].isupper():
    #                 res += rus_upper[((rus_upper.find(f[i]) + n) % mod)]
    #             else:
    #                 res += rus_lower[((rus_lower.find(f[i]) + n) % mod)]

    #     else:
    #         res += f[i]
    # print(res)



# def chifr(word):
#     eng_lower = 'abcdefghijklmnopqrstuvwxyz'
#     eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     symb = [" ", ",", ".", "!", "?", '"']
#     f = word
#     res = ''
#     mod = 26
#     n = len(word)
#     for i in f:
#         if i in symb:
#             n -= 1
#     for i in range(len(f)):
#         if f[i].isalpha():
#             if f[i].isupper():
#                 res += eng_upper[((eng_upper.find(f[i]) + n) % mod)]
#             else:
#                 res += eng_lower[((eng_lower.find(f[i]) + n) % mod)]
#         else:
#             res += f[i]
#     return res

# s = input()
# seq = []
# for i in s.split():
#     seq.append(chifr(i))
# print(*seq)

    

d = {
    "name": "vlad",
    "id": "a",
    "level": 3
    }

print(**d)









