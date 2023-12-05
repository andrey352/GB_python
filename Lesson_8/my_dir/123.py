import os
import json, csv, pickle
from pathlib import Path


# print(Path.cwd())
	
 
path = Path.cwd()
total_size = 0
path, dirs, files = next(os.walk(path))
for f in files:
    fp = os.path.join(path, f)
    print(fp)
    total_size += os.path.getsize(fp)
 
print('Размер каталога (в Кб): ', total_size / 1024)
print('Количество подкаталогов: ', len(dirs))
print('Количество файлов: ', len(files))