# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV

import csv
import json

def json_to_csv(output: str, source: str = 'our_json.json'):
    with open(source, 'r', encoding='utf-8') as src:
        data = json.load(src)
    data = [{'level': level, **user} 
            for level, users in data.items() 
            for user in users]
    with open(output, 'w') as otp:
        writer = csv.DictWriter(otp, ['level', 'id', 'name'])
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    json_to_csv('users_table.csv')
















