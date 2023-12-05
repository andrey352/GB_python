# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Распечатайте его как pickle строку

import pickle
import csv

def csv_to_pickle(source: str):
    with open(source, 'r') as src:
        header = src.readline()[:-1].split(',')
        data = [dict(zip(header, row[:-1].split(','))) for row in src]
        res = pickle.dumps(data)
        print(res)


if __name__ == "__main__":
    csv_to_pickle('pickl_csv.csv')



#  2-й вариант с DictReader

# def csv_to_pickle(source: str):
#     with open(source, 'r') as src:
#         lst = []
#         data = csv.DictReader(src)
#         for line in data:
#             lst.append(line)
#         res = pickle.dumps(lst)
#         print(res)


# if __name__ == "__main__":
#     csv_to_pickle('pickl_csv.csv')




















