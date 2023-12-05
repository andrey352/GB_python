# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки

import json

def json_conv(txt='N&N.txt') -> None:
    with (open('N&N.txt', 'r', encoding='utf-8') as file,
          open('new_file.json', 'w') as new):
        my_dict = {}
        for line in file:
            name, value = line.split()
            my_dict.update({name.capitalize(): float(value[:-2])})
        json.dump(my_dict, new, indent=4)

json_conv()


























