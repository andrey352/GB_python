# Создайте функцию для сортировки файлов по директориям: название директории
#  совпадает с расширением.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки

from pathlib import Path
import os 

def sort_by_dir(directory: Path):
    os.chdir(directory)  
    directories = set(file.suffix 
                      for file in directory.iterdir() 
                      if (file.suffix != '.py' and not file.is_dir()))

    for dir in directories:
        if Path(directory/dir) not in directory.iterdir():
            os.mkdir(dir)

    for file in directory.iterdir():
        if file.suffix and file.suffix != '.py':
            file.replace(f'{file.suffix}/{file.name}')


if __name__ == "__main__":                      # чтобы запуск был из текущей 
    sort_by_dir(Path().cwd())                   # запускаем с терминала

















