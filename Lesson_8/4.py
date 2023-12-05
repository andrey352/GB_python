# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции

# [                                   <- example
#     {
#         'name': 'jon',
#         'id': 234
#         'level': 3
#     }
# ]

import json


def csv_to_json(source: str, output: str):
    with open(source, 'r') as src:
        header = src.readline()[:-1].split(',')
        data = [dict(zip(header, row[:-1].split(','))) for row in src if row != '\n']
    with open(output, 'w') as otp:
        json.dump(manage_data(data), otp, indent=4)


def manage_data(data: list[dict]):
    for user in data:
        user['id'] = f'{user['id']:>010}'
        user['hash'] = hash(user['name']+user['id'])
        user['name'] = user['name'].capitalize()
    return data


if __name__ == '__main__':
    csv_to_json('users_table.csv', 'new_users.json')

















