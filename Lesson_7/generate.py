# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

from string import ascii_lowercase
from random import choice, randint

def filename(min_len, max_len):
    lst = [choice(ascii_lowercase) if i != 2 else choice('aeiouy') for i in range(randint(min_len, max_len))]
    return ''.join(lst)

def make_files(extension: str, 
               min_len: int = 6, 
               max_len: int = 30, 
               min_byte: int = 256, 
               max_byte: int = 1096, 
               count_files: int = 42):
    for _ in range(count_files):
        with open(filename(min_len, max_len) + extension, 'wb') as f:
            bytes_w = bytes([randint(0, 255) for _ in range(randint(min_byte, max_byte+1))])
            f.write(bytes_w)

if __name__ == '__main__':
    make_files('.txt', count_files=3)






















