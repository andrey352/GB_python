# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться

import json
import os

def append_to_json(json_name='our_json.json') -> None:
    if json_name not in os.listdir():
        with open(json_name, 'w') as f:
            json.dump({i: [] for i in range(1, 8)}, f)
    with open(json_name, 'r') as f:
        content = json.load(f)
    user_inp = input('введите имя лич идентификатор и ур доступа: ')
    name, id, acc_lev = user_inp.split()
    content[acc_lev].append({'name': name, 'id': int(id)})
    with open(json_name, 'w') as f:
        json.dump(content, f, indent=4)

while True:
    append_to_json()








