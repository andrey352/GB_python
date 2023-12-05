# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи

__all__ = ["make_files_more_ext"]

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

def make_files_more_ext(*args, **kwargs):           # *args - для позиционных арг-тов
    for ext in args:                                # **kwargs - для ключевых арг-тов
        make_files(ext, **kwargs)


if __name__ == '__main__':
    # make_files('.txt', count_files=5)
    make_files_more_ext('.java', '.mp4', '.jpeg', count_files=1)















