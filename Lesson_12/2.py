# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл

import json
from datetime import datetime


class Factorial:


    def __init__(self, k, path):
        self.path = path
        self.k = k
        self.memoize = []

    def __call__(self, n):
        start = 1
        for i in range (1, n+1):
            start *= i
        self.log(start)
        return start
    
    def log(self, res):
        if len(self.memoize) == self.k:
            self.memoize.pop(0)
        self.memoize.append(res)
    
    def __enter__(self):
        try:
            with open(self.path, 'r') as src:
                self.prev_data = json.load(src)
        except FileNotFoundError:
            with open(self.path, 'w') as trgt:
                self.prev_data = {}
                json.dump({}, trgt)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = {str(datetime.now().__format__('%Y-%m-%d %H:%M')): self.memoize}
        self.prev_data.update(data)
        with open(self.path, 'w') as trgt:
            json.dump(self.prev_data, trgt, indent=4)


if __name__ == "__main__":
    with Factorial(3, 'our_json.json') as f:
        for i in range(2, 5):
            print(f'{f(i) = }, {f.memoize = }')

















