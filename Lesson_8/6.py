# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла

import pickle
import csv

def pickle_to_scv(source: str, output: str):
    with (open(source, 'rb') as src,
          open(output, 'w') as otp):
        data = pickle.load(src)
        headers = list(data[0].keys())
        writer = csv.DictWriter(otp, headers)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    pickle_to_scv('new_users.pickle', 'pickl_csv.csv')















